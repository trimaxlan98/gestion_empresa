#!/bin/bash

# Activar entorno virtual si estás usando uno
# source venv/bin/activate

# Ejecutar PyInstaller
python3 -m PyInstaller --name="GestionClientes" --onedir --windowed \
    --add-data "clientes/templates:clientes/templates" \
    --add-data "clientes/static:clientes/static" \
    --hidden-import=django.contrib.admin \
    --hidden-import=django.contrib.auth \
    --hidden-import=django.contrib.contenttypes \
    --hidden-import=django.contrib.sessions \
    --hidden-import=django.contrib.messages \
    run_app.py

echo "Proceso de empaquetado completado."