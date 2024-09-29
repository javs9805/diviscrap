from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from casas.maxicambios import getMaxicambios
from casas.cambioschaco import getCambiosChaco
import json
app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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
