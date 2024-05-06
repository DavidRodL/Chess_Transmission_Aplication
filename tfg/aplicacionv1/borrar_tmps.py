import shutil
import os
ruta_especifica = '/var/www/html/tfg/aplicacionv1/imagenes/'
ruta_tmp = os.path.join(ruta_especifica, 'tmp')
if os.path.exists(ruta_tmp) and os.path.isdir(ruta_tmp):
    shutil.rmtree(ruta_tmp)
ruta_tmp1 = os.path.join(ruta_especifica, 'tmp1')
if os.path.exists(ruta_tmp1) and os.path.isdir(ruta_tmp1):
    shutil.rmtree(ruta_tmp1)
