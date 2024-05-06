<?php
$command = '/home/david/Downloads/venv/bin/python3 /var/www/html/tfg/aplicacionv1/borrar_tmps.py 2>&1';
set_time_limit(0);
$salida = exec($command);

$command = '/home/david/Downloads/venv/bin/python3 /var/www/html/tfg/aplicacionv1/reiniciar_fen.py 2>&1';
set_time_limit(0);
$salida = exec($command);

$turnPath = '/var/www/html/tfg/aplicacionv1/turn.txt';
$turn = 'b';
file_put_contents($turnPath, $turn);

?>

