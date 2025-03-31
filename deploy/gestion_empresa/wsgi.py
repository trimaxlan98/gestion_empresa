"""
WSGI config for gestion_empresa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Añadir el directorio del proyecto al path
path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
    sys.path.append(path_home)

# Cargar variables de entorno
from dotenv import load_dotenv
env_path = os.path.join(Path(__file__).parents[1], '.env')
load_dotenv(dotenv_path=env_path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_empresa.settings')

application = get_wsgi_application()