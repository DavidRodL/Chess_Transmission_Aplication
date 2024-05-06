fen_texto = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

with open("/var/www/html/tfg/aplicacionv1/FEN.txt", "w") as archivo:
    archivo.write(fen_texto)

print("Texto guardado en FEN.txt exitosamente.")

