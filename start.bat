@echo off

REM Levantar el backend
cd backend
call ..\venv\Scripts\activate.bat
start uvicorn main:app

REM Levantar el frontend
cd ../frontend
npm start
