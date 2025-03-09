from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Creamos el host y el puerto:
APP_HOST = '0.0.0.0'
APP_PORT = 6100
DEV = True # Temporalmente se va a poner en False para evitar problemas de actualizaciones durante el desarrollo.

# Importamos cosas ncesarias: 

# Cargamos la base de datos conectandola con:
DB_NAME = 'proyecto_murcia_definitivo'
DB_USER = 'practica_conectar_python'
DB_PASSWORD = 'Admin123'
DB_HOST = 'localhost'
DB_PORT = 3306

DB_CONNECTION = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Echo=DEV para que al pasar de True a False la maquina se encienda o se apague 
engine = create_engine(DB_CONNECTION, echo=DEV)

