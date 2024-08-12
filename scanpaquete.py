import psutil
import time
from scapy.all import sniff

# Intervalo de actualización en segundos
UPDATE_DELAY = 1

def get_size(bytes):
    """Devuelve el tamaño de los bytes en un formato legible"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# Función para procesar cada paquete capturado
def process_packet(packet):
    print(packet.summary())

# Obtiene las estadísticas de red iniciales
io = psutil.net_io_counters()
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

# Bucle para actualizar las estadísticas de red
while True:
    time.sleep(UPDATE_DELAY)
    io_2 = psutil.net_io_counters()
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
    print(f"Subida: {get_size(io_2.bytes_sent)}, Descarga: {get_size(io_2.bytes_recv)}, "
          f"Velocidad de subida: {get_size(us / UPDATE_DELAY)}/s, "
          f"Velocidad de descarga: {get_size(ds / UPDATE_DELAY)}/s", end="\r")
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv

    # Captura paquetes en tiempo real
    sniff(prn=process_packet, store=False)
