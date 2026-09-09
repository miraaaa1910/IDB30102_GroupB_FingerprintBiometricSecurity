import os
import json
from sklearn.model_selection import train_test_split


# ============================================================
# CONFIGURATION
# ============================================================

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

LABELS = ["Genuine", "Puppet"]


# ============================================================
# LOAD IMAGE INFORMATION
# ============================================================

def load_dataset(dataset_path):
    """
    Load image paths, labels and participant IDs.

    Expected structure:

        dataset/
        ├── Genuine/
        │   ├── P001/
        │   │   ├── image1.png
        │   │   └── image2.png
        │   └── P002/
        │
        └── Puppet/
            ├── P001/
            │   ├── image1.png
            │   └── image2.png
            └── P002/

    Returns:
        records = [
            {
                "path": image_path,
                "label": "Genuine",
                "participant": "P001"
            }
        ]
    """

    records = []

    for label in LABELS:

        label_folder = os.path.join(
            dataset_path,
            label
        )

        if not os.path.isdir(label_folder):
            print(
                f"Warning: folder not found: {label_folder}"
            )
            continue

        for participant in sorted(
            os.listdir(label_folder)
        ):

            participant_folder = os.path.join(
                label_folder,
                participant
            )

            if not os.path.isdir(participant_folder):
                continue

            for filename in sorted(
                os.listdir(participant_folder)
            ):

                if filename.lower().endswith(
                    IMAGE_EXTENSIONS
                ):

                    image_path = os.path.join(
                        participant_folder,
                        filename
                    )

                    records.append({
                        "path": image_path,
                        "label": label,
                        "participant": participant
                    })

    return records


# ============================================================
# PARTICIPANT-LEVEL SPLITTING
# ============================================================

def split_dataset(
    records,
    train_size=0.70,
    validation_size=0.10,
    test_size=0.20,
    random_state=42
):
    """
    Split the dataset into:

        Training   = 70%
        Validation = 10%
        Testing    = 20%

    The split is performed using PARTICIPANT IDs rather
    than individual images.

    This prevents the same participant from appearing
    in multiple datasets.
    """

    if train_size + validation_size + test_size != 1.0:
        raise ValueError(
            "Train, validation and test sizes must add to 1.0"
        )

    # Get unique participant IDs
    participants = sorted(
        set(
            record["participant"]
            for record in records
        )
    )

    print(
        f"Total participants: {len(participants)}"
    )

    # --------------------------------------------------------
    # First split
    #
    # 70% training
    # 30% temporary
    # --------------------------------------------------------

    train_participants, temp_participants = train_test_split(
        participants,
        test_size=(validation_size + test_size),
        random_state=random_state
    )

    # --------------------------------------------------------
    # Second split
    #
    # From the remaining 30%:
    #
    # 1/3 = validation = 10%
    # 2/3 = testing    = 20%
    # --------------------------------------------------------

    validation_ratio = validation_size / (
        validation_size + test_size
    )

    validation_participants, test_participants = train_test_split(
        temp_participants,
        test_size=(1 - validation_ratio),
        random_state=random_state
    )

    # Convert to sets
    train_set = set(train_participants)
    validation_set = set(validation_participants)
    test_set = set(test_participants)

    # --------------------------------------------------------
    # Assign images according to participant
    # --------------------------------------------------------

    train_records = []
    validation_records = []
    test_records = []

    for record in records:

        participant = record["participant"]

        if participant in train_set:
            train_records.append(record)

        elif participant in validation_set:
            validation_records.append(record)

        elif participant in test_set:
            test_records.append(record)

    return (
        train_records,
        validation_records,
        test_records
    )


# ============================================================
# CHECK FOR DATA LEAKAGE
# ============================================================

def check_participant_leakage(
    train_records,
    validation_records,
    test_records
):
    """
    Check that no participant appears in more than one split.
    """

    train_participants = set(
        record["participant"]
        for record in train_records
    )

    validation_participants = set(
        record["participant"]
        for record in validation_records
    )

    test_participants = set(
        record["participant"]
        for record in test_records
    )

    train_validation_overlap = (
        train_participants &
        validation_participants
    )

    train_test_overlap = (
        train_participants &
        test_participants
    )

    validation_test_overlap = (
        validation_participants &
        test_participants
    )

    if (
        train_validation_overlap
        or train_test_overlap
        or validation_test_overlap
    ):
        raise ValueError(
            "DATA LEAKAGE DETECTED! "
            "A participant appears in multiple splits."
        )

    print("\nNo participant leakage detected.")


# ============================================================
# PRINT DATASET INFORMATION
# ============================================================

def print_split_information(
    train_records,
    validation_records,
    test_records
):

    train_participants = set(
        record["participant"]
        for record in train_records
    )

    validation_participants = set(
        record["participant"]
        for record in validation_records
    )

    test_participants = set(
        record["participant"]
        for record in test_records
    )

    print("\n==============================")
    print("DATASET SPLIT")
    print("==============================")

    print(
        f"Training participants: "
        f"{len(train_participants)}"
    )

    print(
        f"Validation participants: "
        f"{len(validation_participants)}"
    )

    print(
        f"Testing participants: "
        f"{len(test_participants)}"
    )

    print()

    print(
        f"Training images: "
        f"{len(train_records)}"
    )

    print(
        f"Validation images: "
        f"{len(validation_records)}"
    )

    print(
        f"Testing images: "
        f"{len(test_records)}"
    )


# ============================================================
# SAVE SPLITS
# ============================================================

def save_splits(
    train_records,
    validation_records,
    test_records,
    output_path="outputs/dataset_splits.json"
):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    split_data = {
        "train": train_records,
        "validation": validation_records,
        "test": test_records
    }

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(
            split_data,
            file,
            indent=4
        )

    print(
        f"\nDataset splits saved to: {output_path}"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    DATASET_PATH = "dataset"

    records = load_dataset(
        DATASET_PATH
    )

    print(
        f"Total images: {len(records)}"
    )

    (
        train_records,
        validation_records,
        test_records
    ) = split_dataset(records)

    print_split_information(
        train_records,
        validation_records,
        test_records
    )

    check_participant_leakage(
        train_records,
        validation_records,
        test_records
    )

    save_splits(
        train_records,
        validation_records,
        test_records
    )
