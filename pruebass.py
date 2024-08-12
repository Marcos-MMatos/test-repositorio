import hashlib

texto = "Hola, mundo"
hash_resultado = hashlib.sha256(texto.encode()).hexdigest()

print(f"SHA-256: {hash_resultado}")
