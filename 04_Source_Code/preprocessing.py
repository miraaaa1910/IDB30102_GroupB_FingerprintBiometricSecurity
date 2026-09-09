import cv2
import numpy as np


# ============================================================
# IMAGE LOADING
# ============================================================

def load_image(image_path):
    """
    Load an image in grayscale.
    """

    image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    if image is None:
        raise ValueError(
            f"Unable to load image: {image_path}"
        )

    return image


# ============================================================
# HISTOGRAM EQUALIZATION
# ============================================================

def histogram_equalization(image):
    """
    Improve the contrast of the fingerprint image.
    """

    equalized = cv2.equalizeHist(
        image
    )

    return equalized


# ============================================================
# GAUSSIAN FILTERING
# ============================================================

def gaussian_filter(
    image,
    kernel_size=(5, 5),
    sigma=0
):
    """
    Reduce image noise using Gaussian filtering.
    """

    filtered = cv2.GaussianBlur(
        image,
        kernel_size,
        sigma
    )

    return filtered


# ============================================================
# ROI SEGMENTATION
# ============================================================

def segment_roi(image):
    """
    Segment the fingerprint region from the background.

    Otsu thresholding and morphological operations are used
    to create the ROI mask.
    """

    # Otsu thresholding
    _, mask = cv2.threshold(
        image,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Morphological operations
    kernel = np.ones(
        (5, 5),
        np.uint8
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:
        return image

    # Largest contour
    largest_contour = max(
        contours,
        key=cv2.contourArea
    )

    # Create ROI mask
    roi_mask = np.zeros_like(
        image
    )

    cv2.drawContours(
        roi_mask,
        [largest_contour],
        -1,
        255,
        thickness=cv2.FILLED
    )

    # Apply mask
    roi = cv2.bitwise_and(
        image,
        image,
        mask=roi_mask
    )

    return roi


# ============================================================
# RESIZE
# ============================================================

def resize_image(
    image,
    size=(224, 224)
):
    """
    Resize image to a fixed size.
    """

    resized = cv2.resize(
        image,
        size
    )

    return resized


# ============================================================
# NORMALIZATION
# ============================================================

def normalize_image(image):
    """
    Scale pixel values from [0,255] to [0,1].
    """

    normalized = (
        image.astype(np.float32)
        / 255.0
    )

    return normalized


# ============================================================
# COMPLETE PREPROCESSING PIPELINE
# ============================================================

def preprocess_image(
    image_path,
    image_size=(224, 224)
):
    """
    Complete preprocessing pipeline:

    1. Load grayscale image
    2. Histogram equalization
    3. Gaussian filtering
    4. ROI segmentation
    5. Resize
    6. Normalization
    """

    image = load_image(
        image_path
    )

    image = histogram_equalization(
        image
    )

    image = gaussian_filter(
        image
    )

    image = segment_roi(
        image
    )

    image = resize_image(
        image,
        image_size
    )

    image = normalize_image(
        image
    )

    return image


# ============================================================
# MAIN TEST
# ============================================================

if __name__ == "__main__":

    print(
        "Preprocessing module loaded successfully."
    )

    print(
        "Functions available:"
    )

    print(
        "- load_image()"
    )

    print(
        "- histogram_equalization()"
    )

    print(
        "- gaussian_filter()"
    )

    print(
        "- segment_roi()"
    )

    print(
        "- resize_image()"
    )

    print(
        "- normalize_image()"
    )

    print(
        "- preprocess_image()"
    )

