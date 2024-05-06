import os
import concurrent.futures
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import chess
import argparse
from itertools import permutations

def load_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise Exception(f"Error al cargar la imagen: {image_path}")
    return img

def image_similarity_ssim(img1, img2):
    return ssim(img1, img2)

def image_similarity_hist(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

def calculate_similarity(image_paths):
    image1_path, image2_path = image_paths
    img1 = load_image(image1_path)
    img2 = load_image(image2_path)

    similarity1 = image_similarity_ssim(img1, img2)

    hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
    similarity2 = image_similarity_hist(hist1, hist2)

    return similarity1, similarity2

def main(fen_initial, turn):
    folder1 = "/var/www/html/tfg/aplicacionv1/imagenes/tmp1/pieces"
    folder2 = "/var/www/html/tfg/aplicacionv1/imagenes/tmp/pieces"
    #folder1 = "/home/david/Downloads/compare_image/tmp1/pieces"
    #folder2 = "/home/david/Downloads/compare_image/tmp2/pieces"

    if not os.path.exists(folder1) or not os.path.exists(folder2):
        print("Al menos una de las carpetas de imágenes no existe.")
        print(fen_initial)
        return
        
    found_valid_move = False

    image_paths = [(os.path.join(folder1, f"_{i}_{j}.jpg"), os.path.join(folder2, f"_{i}_{j}.jpg"))
                   for i in range(8) for j in range(8)]

    threshold = 0.88 		#85
    max_mean_similarity = 0.80	#75

    index_to_chess_notation = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}


    full_fen = f"{fen_initial} {turn} KQkq - 0 1"
    
    new_board = chess.Board(fen=full_fen)

    moves_to_play = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        similarity_results = list(executor.map(calculate_similarity, image_paths))

    print("\nCasillas no similares:")
    for i, (similarity1, similarity2) in enumerate(similarity_results):
        mean_similarity = np.mean((similarity1, similarity2))
        if similarity1 < threshold and similarity2 < threshold and mean_similarity < max_mean_similarity:
            row = i // 8
            col = i % 8
            chess_notation = f"{index_to_chess_notation[col]}{8 - row}"

            moves_to_play.append(chess_notation)

            print(f"{chess_notation}: {similarity1:.2f}%, {similarity2:.2f}%")

    
    for move_from, move_to in permutations(moves_to_play, 2):
    	move_obj1 = chess.Move.from_uci(f"{move_from}{move_to}")
	
    	if move_obj1 in new_board.legal_moves:
            new_board.push(move_obj1)
            new_fen = new_board.fen().split(" ")[0]
            print("Jugada:", move_obj1)
            print(new_fen)
            found_valid_move = True

    if not found_valid_move:
        print("No se encontraron jugadas válidas.")
        print(fen_initial)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Procesar FEN y realizar jugadas basadas en imágenes')
    parser.add_argument('fen', type=str, help='FEN del tablero')
    parser.add_argument('turn', type=str, help='turno de juego')
    args = parser.parse_args()
    main(args.fen, args.turn)

