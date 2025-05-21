import sys
import os

# Ruta al proyecto
project_home = '/home/asistenteia/asistente-ia'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application  # Importa tu app Flask

# Si necesitás configurar variables de entorno:
os.environ['GEMINI_API_KEY'] = 'AIzaSyAFD_0WHxXW44a_QPBswzYp9K0YpW0XZMQ'  # Mejor si lo seteás en el panel AlwaysData
