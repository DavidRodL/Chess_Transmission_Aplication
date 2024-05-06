<?php
$imageData = $_POST['imageData'];
$image = base64_decode(str_replace('data:image/jpeg;base64,', '', $imageData));

$imageNumberPath = '/var/www/html/tfg/aplicacionv1/counter.txt';
$imageNumber = intval(file_get_contents($imageNumberPath));

$imageName = $imageNumber . '.jpg';

$newImageNumber = $imageNumber + 1;
file_put_contents($imageNumberPath, $newImageNumber);

$imagePath = '/var/www/html/tfg/aplicacionv1/imagenes/' . $imageName;

file_put_contents($imagePath, $image);



$fenPath = '/var/www/html/tfg/aplicacionv1/FEN.txt';

$fen = file_get_contents($fenPath);


$directorio = '/home/david/Downloads/LiveChess2FEN/';

chdir($directorio);


$command = '/home/david/Downloads/venv/bin/python3 /var/www/html/tfg/aplicacionv1/renombrar_tmps.py  2>&1';
set_time_limit(0);
$salida = exec($command);

	
$command = '/home/david/Downloads/venv/bin/python3 /home/david/Downloads/LiveChess2FEN/lc2fen.py -o /var/www/html/tfg/aplicacionv1/imagenes/' . $imageName . ' BL 2>&1';

/*
$command = '/home/david/Downloads/venv/bin/python3 /var/www/html/tfg/aplicacionv1/borrar_tmps.py  2>&1';
*/
set_time_limit(0);
$salida = exec($command);	
		
		

$turnPath = '/var/www/html/tfg/aplicacionv1/turn.txt';
$turn = file_get_contents($turnPath);	
		
$command = '/home/david/Downloads/venv/bin/python3 /home/david/Downloads/compare_image/compara_imagenv9_final.py \'' . $fen . '\' \'' . $turn . '\'  2>&1';
$salida = exec($command);

$turn = ($turn === 'w') ? 'b' : 'w';
file_put_contents($turnPath, $turn);
		
$salida_js = json_encode($salida);

file_put_contents($fenPath, $salida);

?>



?>
