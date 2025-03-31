import os
import sys
from pathlib import Path

# Añadir el directorio del proyecto al path
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Establecer la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_empresa.settings')

# Importar el objeto de aplicación WSGI desde el módulo de Django
from gestion_empresa.wsgi import application