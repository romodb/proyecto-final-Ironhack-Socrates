# Este documento recoge la creación de la api, Socrates, al igual que en documentos previos se va a ir documentando todo.
# Importamos cosas para poder proceder:
from fastapi import FastAPI, HTTPException, Response, Status
from fastapi.responses import RedirectResponse
import uvicorn
import pandas as pd

# Creamos el host y el puerto:
HOST = '0.0.0.0'
PORT = 610
DEV = False # Temporalmente se va a poner en False para evitar problemas de actualizaciones durante el desarrollo.
 
# Iniciamos el proceso:




