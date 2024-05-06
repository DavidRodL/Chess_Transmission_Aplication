import os
import concurrent.futures
import cv2
import numpy as np

def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise Exception(f"Error al cargar la imagen: {image_path}")
    return img

def image_similarity_pearson(img1, img2):
    flattened_img1 = img1.flatten()
    flattened_img2 = img2.flatten()
    correlation_matrix = np.corrcoef(flattened_img1, flattened_img2)
    correlation = correlation_matrix[0, 1]
    return correlation

def calculate_similarity(image_paths):
    image1_path, image2_path = image_paths
    img1 = load_image(image1_path)
    img2 = load_image(image2_path)

    similarity_pearson = image_similarity_pearson(img1, img2)

    return similarity_pearson

def main():
    folder1 = "/home/david/Downloads/compare_image/TFG/tmp00/pieces"
    folder2 = "/home/david/Downloads/compare_image/TFG/tmp22/pieces"

    image_paths = [(os.path.join(folder1, f"_{i}_{j}.jpg"), os.path.join(folder2, f"_{i}_{j}.jpg"))
                   for i in range(8) for j in range(8)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        similarity_results = list(executor.map(calculate_similarity, image_paths))

    print("\nTabla de coeficientes de correlación de Pearson:")
    for i in range(8):
        row = ""
        for j in range(8):
            index = i * 8 + j
            similarity_pearson = similarity_results[index]
            row += f"{similarity_pearson:.2f}\t"
        print(row)

if __name__ == "__main__":
    main()

