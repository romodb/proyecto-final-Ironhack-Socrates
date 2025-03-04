# Importamos cosillas necesarias:
import pandas as pd
from sqlalchemy import create_engine, text, Table, MetaData
from sqlalchemy.orm import sessionmaker

# Conectamos a la db: 
data = 'proyecto_murcia'
connection_string = 'mysql+pymysql://practica_conectar_python:Admin123'+'@localhost/'+data
engine = create_engine(connection_string)

# Verificamos la conexion, hacemos una query random:
conexion = engine.connect()
with engine.connect() as connection:
    query_0 = text('SELECT * FROM autores_murcia')
    result = connection.execute(query_0)
    for row in result.mappings():
        print(row)


# Una vez comprobado que está todo conectado ya que la primera query (query_0) va bien 
# procedemos a probar el bucle para conectar las tablas: 
# Cargamos las referencias a la tablas y las propias tablas:
metadata = MetaData()
autores_murcia = Table('autores_murcia', metadata, autoload_with= engine)
obras_arte_murcia = Table('obras_arte_murcia', metadata, autoload_with= engine)

#Creamos un diccionario para "flechar" nombres con id´s:
dicc_autores = {}
with engine.connect() as conexion:
    result = conexion.execute(autores_murcia.select())
    for row in result:
        
        try:
            dicc_autores[row['nombre_autor']] = row['id_autor']
        except KeyError as e:
            print(f"Error al acceder a la columna: {e}, fila: {row}")

# Iniciamos el bucle y actualizamos los nombres por id´s:
with engine.connect() as conexion:
    resultado_1 = conexion.execute(obras_arte_murcia.select())

    for row in resultado_1:
        nom_autor = row['nombre_autor']
        if nom_autor in dicc_autores: 
            id_autor = dicc_autores[nom_autor]
            conexion.execute(
                obras_arte_murcia.update().where(obras_arte_murcia.c.nombre == nom_autor)
                .values(id_autor = id_autor)
            )

# #