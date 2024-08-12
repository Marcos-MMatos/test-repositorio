import socket

def obtener_ip_privada():
    try:
        # Conectar a un servicio externo para determinar la IP privada
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 1))  # Dirección IP arbitraria de Google DNS
        ip_privada = s.getsockname()[0]
        s.close()
        return ip_privada
    except Exception as e:
        print(f"Error al obtener la IP privada: {e}")
        return None

def obtener_nombre_ordenador():
    try:
        # Obtener el nombre del host
        nombre_ordenador = socket.gethostname()
        return nombre_ordenador
    except Exception as e:
        print(f"Error al obtener el nombre del ordenador: {e}")
        return None

if __name__ == "__main__":
    ip_privada = obtener_ip_privada()
    nombre_ordenador = obtener_nombre_ordenador()

    if ip_privada:
        print(f"Tu IP privada es: {ip_privada}")
    if nombre_ordenador:
        print(f"El nombre de tu ordenador es: {nombre_ordenador}")
