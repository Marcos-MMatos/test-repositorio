import shutil
import os
from datetime import datetime
from tqdm import tqdm

def copiar_carpeta(origen, destino):
    try:
        # Crear una marca de tiempo para la copia diaria
        marca_tiempo = datetime.now().strftime("%Y%m%d")
        destino_diario = os.path.join(destino, f'copia_{marca_tiempo}')

        # Obtener lista de archivos y carpetas en el directorio de origen
        items = os.listdir(origen)
        total_items = len(items)

        # Crear el directorio de destino
        os.makedirs(destino_diario, exist_ok=True)

        # Copiar cada archivo y carpeta con una barra de progreso
        with tqdm(total=total_items, desc="Copiando archivos", unit="archivo") as pbar:
            for item in items:
                s = os.path.join(origen, item)
                d = os.path.join(destino_diario, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
                pbar.update(1)

        print(f'Copia completada: {destino_diario}')
    except Exception as e:
        print(f'Error al copiar la carpeta: {e}')

# Directorio de origen y destino
directorio_origen = r'\\172.16.11.13\Monitoreo'
directorio_destino = r'C:\Users\Eliff\OneDrive - Universidad del Magdalena\Documentos\SIIGO'

# Llamar a la función para copiar la carpeta
copiar_carpeta(directorio_origen, directorio_destino)