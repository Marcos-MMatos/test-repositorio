import shutil
import os
from datetime import datetime

def copiar_carpeta(origen, destino):
    try:
        # Crear una marca de tiempo para la copia diaria
        marca_tiempo = datetime.now().strftime("%Y%m%d")
        destino_diario = os.path.join(destino, f'copia_{marca_tiempo}')

        # Copiar la carpeta
        shutil.copytree(origen, destino_diario)
        print(f'Copia completada: {destino_diario}')
    except Exception as e:
        print(f'Error al copiar la carpeta: {e}')

# Directorio de origen y destino
directorio_origen = r'C:\Users\Eliff\Downloads\41EL5N67GAR6ZA445-P'
directorio_destino = r'D:\PRUEBA'

# Llamar a la función para copiar la carpeta
copiar_carpeta(directorio_origen, directorio_destino)
