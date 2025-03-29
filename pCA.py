from sklearn.decomposition import PCA

def apply_pca(image, n_components=1):
    # Flatten the image to apply PCA
    flat_image = image.flatten().reshape(-1, 1)
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(flat_image)
    # Reshape back to the original image shape
    pca_image = pca_result.reshape(image.shape)
    return pca_image