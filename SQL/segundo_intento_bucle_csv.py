# Importamos cosas:
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Definimos el modelo para los autores:
autores = declarative_base()

class Autor(autores):
    __tablename__ = 'autores_murcia'
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String)

# Creamos el motor de conexion:
data = 'proyecto_murcia_definitivo'
DATABASE_URL = f'mysql+pymysql://practica_conectar_python:Admin123@localhost/{data}'
engine = create_engine(DATABASE_URL, echo=True)

# Creamos una sesión:
sesion_0 = sessionmaker(bind=engine)
sesion_1 = sesion_0()

# Cargamos el CSV de los autores:
autores_csv = pd.read_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/obras_arte_murcia.csv')
# Creamos una columna nueva para añadir los id´s:
autores_csv.insert(column='id_autor', value=None, loc=0)

failed = []

# 
for index, row in autores_csv.iterrows():
    autor_nombre = row['nombre_autor']
    # Buscamos el nombre_autor del autor en la db:
    # autor = sesion_1.query(Autor).filter(Autor.nombre_autor == autor_nombre).first()
    autor = sesion_1.query(Autor).filter(Autor.nombre_autor.like(f'%{autor_nombre}%')).first()
    

    if autor:
        # Si existe tiene id_autor:
        autores_csv.at[index, 'id_autor'] = autor.id_autor
    else:
        failed.append(autor_nombre)

# Almacenamos los datos nuevos en un nuevo csv:
autores_csv.to_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/SQL/obras_autor.csv', index=False)

# Cerramos sesión:
sesion_1.close()

[print(f"{a} no esta en nuestra db") for a in failed]


#  Logrado con los autores vamos con los usuarios:
# Definimos el modelo para los autores:
usuario = declarative_base()

class User(usuario):
    __tablename__ = 'usuarios_murcia'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String, unique=True)
    id_inventario = Column(String, unique=True)
    municipio = Column(String)
    pedania  = Column(String)
    direccion = Column(String)
    cp  = Column(String)

# Creamos una columna nueva para añadir los id´s:
datos = 'proyecto_murcia_definitivo'
DATABASE_URL = f'mysql+pymysql://practica_conectar_python:Admin123@localhost/{data}'
engine = create_engine(DATABASE_URL, echo=True)

# Creamos una sesión:
sesion_2 = sessionmaker(bind=engine)
sesion_3 = sesion_2()

# Cargamos el csv de los usuarios:
usuario_csv = pd.read_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/SQL/obras_autor.csv')
# Creamos una columna para añadir los id´s:
usuario_csv.insert(column='id_usuario', value=None, loc=1)

failed = []

# Creamos el bucle para los usuarios:
for index, row in usuario_csv.iterrows():
    usuario_nombre = row['usuario']
    # Buscamos el nombre_autor del autor en la db:
    # autor = sesion_1.query(Autor).filter(Autor.nombre_autor == autor_nombre).first()
    usuario = sesion_1.query(User).filter(User.nombre_usuario.like(f'%{usuario_nombre}%')).first()
    

    if usuario:
        # Si existe tiene id_autor:
        usuario_csv.at[index, 'id_usuario'] = usuario.id_usuario
    else:
        failed.append(usuario_nombre)

# Almacenamos los datos nuevos en un nuevo csv:
usuario_csv.to_csv('C:/Users/Ro/OneDrive/Escritorio/No se como llamarlo/Ironhack/Proyecto final_error_definitivo/SQL/obras_autor.csv', index=False)

[print(f"{a} no esta en nuestra db") for a in failed]

# Cerramos sesión:
sesion_1.close()


