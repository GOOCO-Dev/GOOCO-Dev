def subtract_images(image1, image2):
    # Subtract the pixel values of the two images
    difference_image = np.abs(image1 - image2)
    return difference_image