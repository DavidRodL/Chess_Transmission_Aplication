import os
import concurrent.futures
import cv2
import numpy as np

def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise Exception(f"Error al cargar la imagen: {image_path}")
    return img

def image_similarity_mse(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    return mse

def calculate_similarity(image_paths):
    image1_path, image2_path = image_paths
    img1 = load_image(image1_path)
    img2 = load_image(image2_path)

    similarity_mse = image_similarity_mse(img1, img2)

    return similarity_mse

def main():
    folder1 = "/home/david/Downloads/compare_image/TFG/tmp00/pieces"
    folder2 = "/home/david/Downloads/compare_image/TFG/tmp22/pieces"

    image_paths = [(os.path.join(folder1, f"_{i}_{j}.jpg"), os.path.join(folder2, f"_{i}_{j}.jpg"))
                   for i in range(8) for j in range(8)]

    threshold_difference = 0.6
    threshold_similarity = 0.9

    with concurrent.futures.ThreadPoolExecutor() as executor:
        similarity_results = list(executor.map(calculate_similarity, image_paths))

    print("\nTabla de similitud MSE:")
    for i in range(8):
        row = ""
        for j in range(8):
            index = i * 8 + j
            similarity_mse = similarity_results[index]
            row += f"{similarity_mse:.2f}\t"
        print(row)

if __name__ == "__main__":
    main()

