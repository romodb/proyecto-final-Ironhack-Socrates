# Este documento recoge la creación de la api, Socrates, al igual que en documentos previos se va a ir documentando todo.
# Importamos cosas para poder proceder:
from fastapi import FastAPI, HTTPException, Response, status
from fastapi.responses import RedirectResponse
import uvicorn
import pandas as pd
from sqlalchemy import create_engine, Table, Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Creamos el host y el puerto:
HOST = '0.0.0.0'
PORT = 6100
DEV = True # Temporalmente se va a poner en False para evitar problemas de actualizaciones durante el desarrollo.

# Cargamos la base de datos conectandola con:
data = 'proyecto_murcia_definitivo'
string_conexion = f'mysql+pymysql://practica_conectar_python:Admin123@localhost/{data}'
# contrasena = 'Admin123'
engine = create_engine(string_conexion, echo=True)

# Definimos el modelo para las obras:
obras = declarative_base()

class Obras(obras):
    __tablename__ = 'obras_murcia'
    id_inventario = Column(Integer, primary_key=True)
    titulo = Column(String)
    id_autor = Column(Integer, ForeignKey('autores_murcia.id_autor'))
    fondo_cm = Column(Integer)
    ancho_cm = Column(Integer)
    alto_cm = Column(Integer)
    tecnica = Column(String)
    material_base = Column(String)
    material_secundario = Column(String)
    tematica = Column(String)
    id_usuario = Column(Integer, ForeignKey('usuarios_murcia.id_usuario'))

# Definimos tambien los autores:
autores = declarative_base()

class Autor(autores):
    __tablename__ = 'autores_murcia'
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String)
    # id_inventario = Column(String)

usuario = declarative_base()

class Usuario(usuario):
    __tablename__ = 'usuarios_murcia'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String)
    id_inventario = Column(String)
    municipio = Column(String)
    pedania = Column(String)
    direccion = Column(String)
    cp = Column(String)

# Iniciamos el proceso:
socrates = FastAPI()

@socrates.get("/")
async def root():
    return RedirectResponse('/docs', status_code=303)


# Comenzamos con los endpoint´s:
# La idea es que haya uno por cada acción típica de CRUD, vamos a ir por orden de letras:
# C de Create, para dar de alta obras:
 


# R de Read, para obtener valores de una categoría:
@socrates.get('/datos/autores')
async def datos_autores():
    return autores



# @socrates.get('/datos/usuarios')
# async def datos_usuarios():
#     return usuarios

# @socrates.get('/datos/obras')
# async def datos_obras():
#     return obras_arte

# Para obtener el nombre de un usuario/entidad concreto:
# @socrates.get('datos/{pk}') 

# U de Update, para dar de alta un csv nuevo y así agregar valores en una tabla:


# D de Delete, para eliminar valores:





if __name__ == '__main__':
    uvicorn.run(app='Socrates:socrates', host=HOST, port=PORT, reload=DEV)





pp/
 | - main.py
 | - dao/
      | -> dao.py
 | - models/
      | -> models.py
 | - settings/
      | -> setting.py
 | - routers/
      | -> router1.py
      | -> router2.py
      | -> routerN.py
