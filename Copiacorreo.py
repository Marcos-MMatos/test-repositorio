import os
import shutil
from datetime import datetime
from tqdm import tqdm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_notificacion(asunto, cuerpo, destinatario):
    remitente = 'zafarismarcos@outlook.com'
    contraseña = 'M4rc0s.M4t0s'  # Reemplaza con tu contraseña de Outlook

    # Configurar el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Adjuntar el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        # Conectar al servidor de Outlook
        servidor = smtplib.SMTP('smtp.office365.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        texto = mensaje.as_string()
        servidor.sendmail(remitente, destinatario, texto)
        servidor.quit()
        print(f'Correo enviado a {destinatario}')
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

def copiar_carpeta(origen, destino):
    try:
        marca_tiempo = datetime.now().strftime("%Y%m%d")
        destino_diario = os.path.join(destino, f'copia_{marca_tiempo}')

        items = os.listdir(origen)
        total_items = len(items)

        os.makedirs(destino_diario, exist_ok=True)

        with tqdm(total=total_items, desc="Copiando archivos", unit="archivo") as pbar:
            for item in items:
                s = os.path.join(origen, item)
                d = os.path.join(destino_diario, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
                pbar.update(1)

        # Enviar notificación de éxito
        asunto = f"Copia SIIGO completada: {marca_tiempo}"
        cuerpo = f"La copia de la carpeta se completó exitosamente.\nDestino: {destino_diario}"
        enviar_notificacion(asunto, cuerpo, 'zafarismarcos@outlook.com')

        print(f'Copia completada: {destino_diario}')
    except Exception as e:
        # Enviar notificación de error
        asunto = f"Error al copiar la carpeta: {marca_tiempo}"
        cuerpo = f"Ocurrió un error al copiar la carpeta:\n{e}"
        enviar_notificacion(asunto, cuerpo, 'zafarismarcos@outlook.com')

        print(f'Error al copiar la carpeta: {e}')

# Directorio de origen y destino
directorio_origen = r'C:\Users\Eliff\OneDrive - Universidad del Magdalena\Documentos\Reflect'
directorio_destino = r'C:\Users\Eliff\OneDrive - Universidad del Magdalena\Documentos\INTENTO NUMERO 1'

# Llamar a la función para copiar la carpeta
copiar_carpeta(directorio_origen, directorio_destino)
