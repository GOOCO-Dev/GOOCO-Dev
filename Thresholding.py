def apply_threshold(image, threshold_value):
    # Apply a threshold to isolate significant changes
    _, thresholded_image = cv2.threshold(image, threshold_value, 1, cv2.THRESH_BINARY)
    return thresholded_image