import cv2
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Normalize the pixel values to [0, 1]
    normalized_image = gray_image / 255.0
    return normalized_image

def subtract_images(image1, image2):
    # Subtract the pixel values of the two images
    difference_image = np.abs(image1 - image2)
    return difference_image

def apply_pca(image, n_components=1):
    # Flatten the image to apply PCA
    flat_image = image.flatten().reshape(-1, 1)
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(flat_image)
    # Reshape back to the original image shape
    pca_image = pca_result.reshape(image.shape)
    return pca_image

def apply_threshold(image, threshold_value):
    # Apply a threshold to isolate significant changes
    _, thresholded_image = cv2.threshold(image, threshold_value, 1, cv2.THRESH_BINARY)
    return thresholded_image

def morphological_operations(image):
    # Apply dilation and erosion to refine detected areas
    kernel = np.ones((3, 3), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)
    return eroded_image

def visualize_deforestation_map(deforestation_map):
    plt.imshow(deforestation_map, cmap='gray')
    plt.title("Deforestation Map")
    plt.show()

def detect_deforestation(image_before_path, image_after_path, threshold_value):
    # Step 1: Preprocess the images
    image_before = preprocess_image(image_path="E:\\BSE22\\other\\deforestation\\IMG_20250303_204536_006.jpg")
    image_after = preprocess_image(image_path="E:\\BSE22\\other\\deforestation\\IMG_20250303_204533_502.jpg")
    
    # Step 2: Perform image differencing
    difference_image = subtract_images(image_after, image_before)
    
    # Step 3: Apply PCA to reduce dimensionality
    pca_image = apply_pca(difference_image)
    
    # Step 4: Apply thresholding
    deforestation_map = apply_threshold(pca_image, threshold_value)
    
    # Step 5: Post-processing
    refined_deforestation_map = morphological_operations(deforestation_map)
    
    return refined_deforestation_map

# Example usage
image_before_path = 'E:\\BSE22\\other\\deforestation\\IMG_20250303_204536_006.jpg'
image_after_path = 'E:\\BSE22\\other\\deforestation\\IMG_20250303_204533_502.jpg'
threshold_value = 0.5
deforestation_map = detect_deforestation(image_before_path, image_after_path, threshold_value)
visualize_deforestation_map(deforestation_map)