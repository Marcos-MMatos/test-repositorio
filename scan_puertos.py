import socket

def escanear_puertos(host, puerto_inicial, puerto_final):
    print(f"Escaneando host: {host}")
    
    for puerto in range(puerto_inicial, puerto_final + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.02)
        resultado = sock.connect_ex((host, puerto))
        
        if resultado == 0:
            print(f"Puerto {puerto}: ABIERTO")
        else:
            print(f"Puerto {puerto}: CERRADO")
        
        sock.close()

# Ejemplo de uso
host = "192.168.18.11"
puerto_inicial = 1
puerto_final = 1024

escanear_puertos(host, puerto_inicial, puerto_final)
