import smtplib
from email.message import EmailMessage
import os
import random
import time
import json

def enviar_email(destinatario, asunto, cuerpo, cv_path, remitente, password, smtp_host='smtp.gmail.com', smtp_port=587):
    # Crear el mensaje
    mensaje = EmailMessage()
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje.set_content(cuerpo)

    # Adjuntar CV
    if cv_path and os.path.exists(cv_path):
        with open(cv_path, 'rb') as cv:
            mensaje.add_attachment(cv.read(), maintype='application', subtype='pdf', filename=os.path.basename(cv_path))
    else:
        print(f"No se encontró el CV en la ruta: {cv_path}")

    # Enviar el correo
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()  # Iniciar conexión segura
            server.login(remitente, password)
            server.send_message(mensaje)
            print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Descripción de quien eres (enfocada en tus habilidades y servicios)
quien_soy = [
    """
    Estimado/a {empresa}:

    Mi nombre es [Tu Nombre] y soy desarrollador web full stack con experiencia en la creación de aplicaciones web modernas, escalables y funcionales. Durante mi carrera, he trabajado con tecnologías como React, Node.js y bases de datos SQL/NoSQL, siempre con el objetivo de optimizar la experiencia de usuario y la eficiencia del backend.

    Me gustaría postularme para colaborar en los proyectos de {empresa}, ofreciendo soluciones innovadoras que se alineen con las necesidades específicas del equipo.

    Adjunto mi CV para que puedas conocer más sobre mi experiencia y habilidades. Quedo a disposición para conversar más sobre cómo puedo contribuir.

    Atentamente,
    [Tu Nombre]
    """
]

# Variaciones del asunto
asuntos = [
    "Desarrollador Web Full Stack",
    "Web Developer"
]

# Ruta del CV (asegúrate de que esté en la misma carpeta o especifica la ruta completa)
cv_path = "ruta/a/tu/cv.pdf"

# Cargar los destinatarios desde el archivo JSON
json_file = 'emails_enviados.json'

# Leer el archivo JSON y cargar los destinatarios
with open(json_file, 'r', encoding='utf-8') as f:
    destinatarios = json.load(f)

# Parámetros de control
BLOQUE_TAMANO = 10
PAUSA_SEGUNDOS = 60  # Ajusta el tiempo de espera entre bloques

# Credenciales y configuración del servidor (sustituir con tus valores)
remitente = 'tu_correo@gmail.com'  # Sustituye con tu correo
password = 'tu_contraseña_de_aplicación'  # Sustituye con la contraseña de la aplicación

# Enviar correos en bloques
for i in range(0, len(destinatarios), BLOQUE_TAMANO):
    bloque = destinatarios[i:i + BLOQUE_TAMANO]
    for destinatario in bloque:
        email = destinatario["email"]
        empresa = destinatario["empresa"]
        asunto = random.choice(asuntos)
        cuerpo = random.choice(quien_soy).format(empresa=empresa)
        enviar_email(email, asunto, cuerpo, cv_path, remitente, password)

    print(f"Bloque de {len(bloque)} correos enviado. Esperando {PAUSA_SEGUNDOS} segundos antes de continuar...")
    time.sleep(PAUSA_SEGUNDOS)
 #GRACIAS