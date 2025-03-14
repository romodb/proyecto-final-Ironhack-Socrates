from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel


db = declarative_base()


class AutorRead(BaseModel):
    id: int
    nombre: str


class AutorCreate(BaseModel):
    nombre: str


class AutorDB(db):
    __tablename__ = 'autores_murcia'
    id_autor = Column(Integer, primary_key=True)
    nombre_autor = Column(String, unique=True)

    def as_base_model(self) -> AutorRead:
        return AutorRead(id=self.id_autor, nombre=self.nombre_autor)
    
