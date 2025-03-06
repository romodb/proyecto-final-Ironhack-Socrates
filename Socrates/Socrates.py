# Este documento recoge la creación de la api, Socrates, al igual que en documentos previos se va a ir documentando todo.
# Importamos cosas para poder proceder:
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.responses import RedirectResponse
import uvicorn
import pandas as pd

# Creamos el host y el puerto:
HOST = '0.0.0.0'
PORT = 610
DEV = False # Temporalmente se va a poner en False para evitar problemas de actualizaciones durante el desarrollo.

# Cargamos la base de datos:
autores = pd.read_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/id_autores_murcia.csv') 
usuarios = pd.read_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/id_entidades_murcia.csv')
obras_arte = pd.read_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/SQL/obras_autor.csv')

# Iniciamos el proceso:
socrates = FastAPI()
# uvicorn.run(app='main:app', host=HOST, port=PORT, reload=DEV)

@socrates.get("/")
async def root():
    return RedirectResponse('/docs', status_code=303)


# Comenzamos con los endpoint´s:
# La idea es que haya uno por cada acción típica de CRUD, vamos a ir por orden de letras:
# C de Create, para dar de alta obras:
 


# R de Read, para obtener valores de una categoría:



# U de Update, para dar de alta un csv nuevo y así agregar valores en una tabla:


# D de Delete, para eliminar valores:

