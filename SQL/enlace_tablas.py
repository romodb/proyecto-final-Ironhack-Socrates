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
        #print(f"Tipo de row: {type(row)}")  
        #print(f"Contenido de row: {row}")  

# Validación para asegurarnos de que row[0] es un nombre (cadena) y row[1] es un id (número)
        try:
            # Verificamos que row[0] no está vacío y es un nombre válido (cadena de texto)
            if isinstance(row[0], str) and row[0].strip() != "":
                nom_autor = row[0]
            else:
                print(f"Advertencia: El valor de nombre del autor no es válido: {row[0]}")
                continue  # Si no es válido, pasamos a la siguiente fila
        # Verificamos que row[1] es un id válido (número entero o float)
            if isinstance(row[1], (int, float)) and row[1] > 0:
                id_autor = row[1]
            else:
                print(f"Advertencia: El valor de id_autor no es válido: {row[1]}")
                continue  # Si no es válido, pasamos a la siguiente fila

            # Si las validaciones pasan, agregamos al diccionario
            dicc_autores[nom_autor] = id_autor
            print(dicc_autores)

        except Exception as e:
            print(f"Error al procesar la fila: {e}, fila: {row}")


        try:
            dicc_autores[row[0]] = row[1] # 0 para el nombre del autor y 1 para el id
        except KeyError as e:
            print(f"Error al acceder a la columna: {e}, fila: {row}")



# Iniciamos el bucle y actualizamos los nombres por id´s:
with engine.connect() as conexion:
    resultado_1 = conexion.execute(obras_arte_murcia.select())

    for row in resultado_1:
        nombre_autor = row[0]
        if nombre_autor in dicc_autores: 
            # Sacamos el id correspondiente al autor:
            id_autor = dicc_autores[nombre_autor]
            # Actualizamos el registro con el id:
            conexion.execute(
                obras_arte_murcia.update().where(obras_arte_murcia.c.nombre_autor == nombre_autor)
                .values(id_autor == id_autor)
            )

# Probamos cosas: 
#with engine.connect() as connection:
#  query = text('SELECT * FROM obras_arte_murcia')
#  result = connection.execute(query)
#  for row in result.mappings():
#      print(row)

# resultado_1
dicc_autores

# #