# from app.ajustes.settings import DB_CONNECTION, DB_USER,DB_HOST,DB_NAME, DB_PASSWORD, DB_PORT

# Definimos la tabla de los autores:
autores = declarative_base()

class Autor(autores):
    __tablename__ = 'autores_murcia'
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String)
    # id_inventario = Column(String)
