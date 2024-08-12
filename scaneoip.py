from scapy.all import ARP, Ether, srp

def escanear_red(red):
    # Crear un paquete ARP request
    arp = ARP(pdst=red)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    paquete = ether/arp

    # Enviar el paquete y recibir las respuestas
    resultado = srp(paquete, timeout=3, verbose=0)[0]

    # Procesar las respuestas
    dispositivos = []
    for enviado, recibido in resultado:
        dispositivos.append({'ip': recibido.psrc, 'mac': recibido.hwsrc})

    return dispositivos

if __name__ == "__main__":
    red = "192.168.18.0/24"  # Cambia esto según el rango de tu red
    dispositivos = escanear_red(red)

    if dispositivos:
        print("Dispositivos encontrados en la red:")
        for dispositivo in dispositivos:
            print(f"IP: {dispositivo['ip']}, MAC: {dispositivo['mac']}")
    else:
        print("No se encontraron dispositivos en la red.")
