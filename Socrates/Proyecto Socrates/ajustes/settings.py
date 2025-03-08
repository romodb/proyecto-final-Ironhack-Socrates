# Creamos el host y el puerto:
HOST = '0.0.0.0'
PORT = 6100
DEV = True # Temporalmente se va a poner en False para evitar problemas de actualizaciones durante el desarrollo.

# Importamos cosas ncesarias: 
import pandas as pd
from sqlalchemy import create_engine, Table, Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Cargamos la base de datos conectandola con:
data = 'proyecto_murcia_definitivo'
string_conexion = f'mysql+pymysql://practica_conectar_python:Admin123@localhost/{data}'
# contrasena = 'Admin123'
engine = create_engine(string_conexion, echo=True)

