import socket

def obtener_ip_de_host(hostname):
    try:
        # Resolver el nombre del host a dirección IP
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.error as e:
        print(f"Error al resolver el nombre del host: {e}")
        return None

if __name__ == "__main__":
    hostname = "eliff"  # Cambia esto por el nombre del host del otro equipo
    ip = obtener_ip_de_host(hostname)

    if ip:
        print(f"La IP del host {hostname} es: {ip}")
