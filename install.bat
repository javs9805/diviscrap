@echo off

REM Crear entorno virtual y activarlo
python -m venv venv
venv\Scripts\activate.bat

REM Instalar dependencias de Python
pip install -r requirements.txt

REM Instalar dependencias del frontend
cd frontend
npm install

REM Terminado
