@echo off

echo Instalar dependencias del frontend
cd frontend
start cmd /c "npm install"
cd ..

echo Crear entorno virtual y activarlo
python -m venv venv
call venv\Scripts\activate.bat

echo Instalar dependencias de Python
pip install -r requirements.txt


echo Terminado
