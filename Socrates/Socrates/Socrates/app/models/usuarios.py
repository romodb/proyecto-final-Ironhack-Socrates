from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

db = declarative_base()

class UsuarioDB(db):
    __tablename__ = 'usuarios_murcia'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String)
    id_inventario = Column(String)
    municipio = Column(String)
    pedania = Column(String)
    direccion = Column(String)
    cp = Column(String)
