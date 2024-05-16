Para utilizar la aplicación web, es necesario realizar los siguientes pasos en una
máquina con un sistema operativo Linux:

1. Primeramente hay que descargar el programa LiveChess2FEN, disponible
en el siguiente enlace:
https://github.com/davidmallasen/LiveChess2FEN/tree/master y realizar la
instalación de los requerimientos especificados en dicho repositorio.
Preferiblemente, a la hora de instalar las librerías de Python necesarias, es
recomendable hacerlo en un entorno virtual.

2. Debido a que la aplicación web está desarrollada en PHP, hay que
instalar Apache y php, para esto se puede ejecutar el siguiente
comando en la terminal: sudo apt update && sudo apt install apache2
php libapache2-mod-php.

3. Tras esta instalación, reiniciamos apache con: sudo systemctl restart
apache2.

4. Después debemos descargar la aplicación web y el programa de Python
compare_image, disponible en el siguiente enlace:
https://github.com/DavidRodL/Chess_Transmission_Aplication

5. Tras la descarga, deberemos mover la carpeta tfg a la siguiente ruta:
/var/www/html y la carpeta compare_image la dejaremos en descargas,
junto con la carpeta LiveChess2FEN (descargada en el paso 1).

6. A las carpetas mencionadas en el apartado anterior, hay que otorgarles
todos los permisos (escritura, lectura y ejecución) para cualquier usuario.

7. Es necesario cambiar las rutas de direcciones de los archivos .php y de
compara_imagenv9_final.py para que se ajusten a las de la máquina en
la que se ejecute.

8. Para utilizar la aplicación, es necesario colocar una cámara encima del
tablero, por lo que si no se tiene ninguna cámara, se pueden utilizar
aplicaciones que conecten la cámara del teléfono con la máquina
como (droidcam).

9. Tras realizar los pasos anteriores, hay que abrir un navegador y escribir:
http://localhost/tfg/aplicacionv1/ y ya tendremos la aplicación web en
funcionamiento.
