import hashlib

def ataque_diccionario(hash_contraseña, archivo_diccionario):
    # Lee el archivo de diccionario línea por línea
    with open(archivo_diccionario, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Elimina posibles espacios en blanco
            palabra = linea.strip()
            
            # Genera el hash SHA-256 de la palabra
            hash_palabra = hashlib.sha256(palabra.encode()).hexdigest()
            
            # Compara el hash generado con el hash de la contraseña
            if hash_palabra == hash_contraseña:
                print(f"Contraseña encontrada: {palabra}")
                return palabra
    
    print("No se encontró la contraseña.")
    return None

# Ejemplo de uso
# Supongamos que la contraseña correcta es 'password123'
# Su hash SHA-256 es 'b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79'
hash_contraseña = "b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79"
archivo_diccionario = "diccionario.txt"  # El archivo debe contener una lista de posibles contraseñas

ataque_diccionario(hash_contraseña, archivo_diccionario)
