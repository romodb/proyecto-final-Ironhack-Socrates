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
