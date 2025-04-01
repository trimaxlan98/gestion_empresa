# run_app.py
import os
import sys
import webbrowser
import threading
import time
from waitress import serve
from gestion_empresa.wsgi import application

# Configuración de entorno
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_empresa.settings')

# Dirección IP y puerto para el servidor
HOST = '0.0.0.0'  # Acepta conexiones desde cualquier dirección en la red local
PORT = 8000

def open_browser():
    """Abre el navegador después de un corto retraso"""
    time.sleep(1.5)  # Esperar a que el servidor esté completamente iniciado
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == '__main__':
    # Información de inicio
    print(f"Iniciando Gestión de Clientes en http://{HOST}:{PORT}")
    print("Presiona Ctrl+C para detener el servidor")
    
    # Abrir el navegador automáticamente
    threading.Thread(target=open_browser).start()
    
    # Iniciar el servidor
    try:
        serve(application, host=HOST, port=PORT, threads=4)
    except KeyboardInterrupt:
        print("\nServidor detenido")
        sys.exit(0)