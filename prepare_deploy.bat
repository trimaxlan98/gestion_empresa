@echo off
REM Script para preparar la aplicación para despliegue en Windows

echo Creando carpeta static si no existe...
if not exist static mkdir static

echo Copiando settings_local.py...
copy settings_local.py gestion_empresa\settings_local.py

echo Instalando dependencias...
pip install -r requirements.txt

echo Recolectando archivos estáticos...
python manage.py collectstatic --settings=gestion_empresa.settings_local --noinput

echo Comprobando migraciones...
python manage.py makemigrations --settings=gestion_empresa.settings_local
python manage.py migrate --settings=gestion_empresa.settings_local --check

echo Creando carpeta para producción...
if not exist deploy mkdir deploy

echo Copiando archivos para producción...
xcopy /E /Y clientes deploy\clientes\
xcopy /E /Y gestion_empresa deploy\gestion_empresa\
xcopy /E /Y media deploy\media\
xcopy /E /Y staticfiles deploy\staticfiles\
copy manage.py deploy\
copy requirements.txt deploy\
copy .env.example deploy\.env.example
copy passenger_wsgi.py deploy\
copy .htaccess deploy\

echo Creando archivo para despliegue...
cd deploy
if exist ..\gestion_clientes.zip del ..\gestion_clientes.zip
powershell -command "Compress-Archive -Path * -DestinationPath ..\gestion_clientes.zip"
cd ..

echo.
echo ¡Preparación completada!
echo Archivo gestion_clientes.zip listo para subir a Hostinger.
echo.
echo IMPORTANTE: No olvides crear y configurar el archivo .env en el servidor con tus variables de entorno.
pause