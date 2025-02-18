
# Envío Automático de Correos con CV Adjunto

Este proyecto permite enviar correos electrónicos automáticamente a una lista de destinatarios utilizando un servidor SMTP, adjuntando un CV en formato PDF. Es ideal para realizar postulaciones laborales masivas de manera eficiente.

**Nota**: Este script incluye una lista de más de **700 correos** de **importantes empresas**, lo que permite realizar envíos masivos a organizaciones destacadas con facilidad. Ejemplos de empresas en la lista:

```json
[
    { "email": "empleos@siemens.com", "empresa": "Siemens" },
    { "email": "rrhh@bosch.com", "empresa": "Bosch" },
    { "email": "reclutamiento@pfizer.com", "empresa": "Pfizer" }
]
```

## Requisitos

Antes de ejecutar el script, asegúrate de tener lo siguiente:

- Python 3.x instalado.
- Acceso a un servidor SMTP (en este caso se utiliza Gmail).
- Un archivo de destinatarios en formato JSON con los correos y nombres de empresas.
- Un CV en formato PDF que deseas adjuntar a los correos.

## Instalación

1. Clona este repositorio o descarga los archivos a tu máquina local.

2. Asegúrate de tener las siguientes bibliotecas instaladas. Si no las tienes, puedes instalarlas usando `pip`:

```bash
pip install smtplib email os random time json
```

3. Configura el archivo de destinatarios en formato JSON con la siguiente estructura:

```json
[
    {
        "email": "ejemplo@empresa.com",
        "empresa": "Empresa Ejemplo"
    },
    {
        "email": "contacto@otraempresa.com",
        "empresa": "Otra Empresa"
    }
]
```

Guarda este archivo como `emails_enviados.json`.

## Configuración del Script

Antes de ejecutar el script, realiza las siguientes configuraciones:

1. **Ruta del CV**: En la variable `cv_path`, proporciona la ruta al archivo PDF que deseas adjuntar. Asegúrate de que el archivo esté en la misma carpeta o proporciona la ruta completa.

```python
cv_path = "ruta/a/tu/cv.pdf"
```

2. **Credenciales del remitente**: En las variables `remitente` y `password`, ingresa tu correo electrónico y la contraseña de la aplicación (si usas Gmail, crea una [contraseña de aplicación](https://support.google.com/accounts/answer/185833?hl=es) para mayor seguridad).

```python
remitente = 'tu_correo@gmail.com'
password = 'tu_contraseña_de_aplicación'
```

## ¿Cómo Funciona?

1. **Lectura de destinatarios**: El script lee un archivo JSON con la lista de destinatarios. Cada destinatario debe contener un correo electrónico y el nombre de la empresa.

2. **Generación del correo**: El cuerpo del correo está basado en una plantilla que incluye el nombre de la empresa, y el asunto es aleatorio entre dos opciones. Además, el CV especificado se adjunta al correo.

3. **Envío de correos**: Los correos se envían en bloques (por defecto, 10 correos por bloque), con un intervalo de espera configurable entre bloques.

4. **Configuración de servidor SMTP**: El script usa el servidor SMTP de Gmail para enviar los correos. La configuración por defecto está en el script, pero puedes cambiar el servidor SMTP y el puerto si lo deseas.

## Ejecución

Una vez que hayas configurado el script y los archivos necesarios, simplemente ejecuta el script desde la terminal:

```bash
python script.py
```

El script enviará los correos uno por uno, adjuntando tu CV y personalizando cada correo con el nombre de la empresa del destinatario.

## Personalización

- Puedes ajustar el tamaño de los bloques de correos modificando la variable `BLOQUE_TAMANO` en el script.
- La pausa entre el envío de bloques de correos se puede modificar a través de la variable `PAUSA_SEGUNDOS`.

## Seguridad

- Asegúrate de usar una contraseña de aplicación para tu cuenta de Gmail para evitar compartir tu contraseña de cuenta principal.
- No compartas tu archivo `emails_enviados.json` ni tus credenciales de correo.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles. Se requiere mantener el reconocimiento al autor y enlazar al repositorio original en cualquier uso o distribución.

aprovechalo al maximo y agradeceme en mi instagram zekecabre6
```
GRACIAS
```

## Palabras clave generales sobre el propósito del proyecto:
Automatización
Envío automático de correos
Automatización de CV
Envío masivo de correos
Automatización de reclutamiento
Correo masivo con Python
Envío de emails automatizado
Enviar CV a empresas automáticamente
Envío automático de curriculum
Palabras clave relacionadas con el uso:
Curriculum Vitae
Aplicación para enviar CV
Aplicación de envío masivo de correos
Envío de correos con Python
Enviar CV a empresas
Automático
Automatización de procesos
Enviar CV por correo electrónico
Herramienta para enviar CV
Tecnologías utilizadas:
Python
SMTP
Email automation with Python
Automated email sending script
Correo electrónico Python
SMTP server Python
Envío de correos con Python
Scripts Python para enviar correos
Enviar emails desde Python
Automatización con Python
Python para enviar correos masivos
Palabras clave relacionadas con el proyecto:
Open-source
Contribuciones a la comunidad
Proyecto para desarrolladores
Automatización para reclutadores
Software para envío de correos masivos
Script Python para email marketing
Envío de correos automatizado con Python
Proyecto de automatización de correos electrónicos
Repositorio de código para enviar CV


## Descargo de responsabilidad
Este código ha sido desarrollado con fines educativos y de contribución a la comunidad. No soy responsable del uso que se le pueda dar a este proyecto, ni de las consecuencias que puedan surgir al utilizarlo. Se ofrece como una herramienta para aprender y mejorar las habilidades de programación.

El uso de este código es bajo tu propio riesgo.

Además, la lista de correos electrónicos incluida en este repositorio tiene fines meramente informativos y no soy responsable de su uso. Los correos electrónicos proporcionados son solo un recurso y no garantizan que sean apropiados o válidos para cualquier propósito. Es responsabilidad del usuario utilizar esta información de manera ética y legal.
