import os
import concurrent.futures
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise Exception(f"Error al cargar la imagen: {image_path}")
    return img

def image_similarity_ssim(img1, img2):
    return ssim(img1, img2)

def image_similarity_hist(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

def image_similarity_pearson(img1, img2):
    flattened_img1 = img1.flatten()
    flattened_img2 = img2.flatten()
    correlation_matrix = np.corrcoef(flattened_img1, flattened_img2)
    correlation = correlation_matrix[0, 1]
    return correlation

def image_similarity_mse(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    return mse

def calculate_similarity(image_paths):
    image1_path, image2_path = image_paths
    img1 = load_image(image1_path)
    img2 = load_image(image2_path)

    similarity_ssim = image_similarity_ssim(img1, img2)
    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
    similarity_hist = image_similarity_hist(hist1, hist2)
    similarity_pearson = image_similarity_pearson(img1, img2)
    similarity_mse = image_similarity_mse(img1, img2)

    return similarity_ssim, similarity_hist, similarity_pearson, similarity_mse

def main():
    folder1 = "/var/www/html/tfg/aplicacionv1/imagenes/tmp1/pieces"
    folder2 = "/var/www/html/tfg/aplicacionv1/imagenes/tmp/pieces"

    image_paths = [(os.path.join(folder1, f"_{i}_{j}.jpg"), os.path.join(folder2, f"_{i}_{j}.jpg"))
                   for i in range(8) for j in range(8)]

    threshold_difference = 0.6
    threshold_similarity = 0.9

    with concurrent.futures.ThreadPoolExecutor() as executor:
        similarity_results = list(executor.map(calculate_similarity, image_paths))

    # Get the x lowest Pearson correlation coefficient value
    x_lowest_pearson = sorted(similarity_results, key=lambda x: x[2])[21][2]

    print("\nLista de porcentajes de similitud:")
    for i, (similarity_ssim, similarity_hist, similarity_pearson, similarity_mse) in enumerate(similarity_results):
        difference = (1 - similarity_ssim) * (1 - similarity_hist) * (1 - similarity_pearson) * similarity_mse
        if (difference > threshold_difference) and \
           (similarity_ssim < threshold_similarity) and \
           (similarity_hist < threshold_similarity) and \
           (similarity_pearson < threshold_similarity) and \
           (similarity_pearson < x_lowest_pearson):
            print(f"_{i//8}_{i%8}: No similar (Difference: {difference:.2f}, "
                  f"SSIM: {similarity_ssim:.2f}, Hist: {similarity_hist:.2f}, Pearson: {similarity_pearson:.2f}, MSE: {similarity_mse:.2f}, x: {x_lowest_pearson:.2f})")
        else:
            print(f"_{i//8}_{i%8}: Similar (Difference: {difference:.2f}, "
                  f"SSIM: {similarity_ssim:.2f}, Hist: {similarity_hist:.2f}, Pearson: {similarity_pearson:.2f}, MSE: {similarity_mse:.2f})")

if __name__ == "__main__":
    main()

