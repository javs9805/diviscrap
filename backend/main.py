from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from casas.maxicambios import getMaxicambios
from casas.cambioschaco import getCambiosChaco
from casas.cambiosAlberdi import getCambiosAlberdi
import json
app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://diviscrap.vercel.app",
    "https://diviscrap-git-main-javs9805s-projects.vercel.app",
    
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_root() -> dict:
    return {"message": "Welcome to Diviscrap."}

@app.get("/casa/maxicambios/")
async def getCasaMaxiCambios():
    return json.loads(getMaxicambios())

@app.get("/casa/cambioschaco/")
async def getCasaCambiosChaco():
    return json.loads(getCambiosChaco())

@app.get("/casa/cambiosalberdi/")
async def getCasaCambiosAlberdi():
    return json.loads(getCambiosAlberdi())