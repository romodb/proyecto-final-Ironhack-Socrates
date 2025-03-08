# Definimos tambien los autores:
autores = declarative_base()

class Autor(autores):
    __tablename__ = 'autores_murcia'
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String)
    # id_inventario = Column(String)
