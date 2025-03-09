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
