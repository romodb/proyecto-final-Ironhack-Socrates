from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


db = declarative_base()


class ObraRead(BaseModel):
    id: int
    titulo: str 
    id_autor: int
    fondo_cm: int
    ancho_cm: int
    alto_cm: int
    tecnica: str | None
    material_base: str | None
    material_secundario: str | None
    tematica: str | None
    id_usuario: int




class ObraDB(db):
    __tablename__ = 'obras_murcia'
    id_inventario = Column(Integer, primary_key=True)
    titulo = Column(String)
    id_autor = Column(Integer)#, ForeignKey('autores_murcia.id_autor'))
    fondo_cm = Column(Integer)
    ancho_cm = Column(Integer)
    alto_cm = Column(Integer)
    tecnica = Column(String)
    material_base = Column(String)
    material_secundario = Column(String)
    tematica = Column(String)
    id_usuario = Column(Integer)#, ForeignKey('usuarios_murcia.id_usuario'))

    def as_base_model(self) -> ObraRead:
        return ObraRead(id=self.id_inventario,
                        titulo=self.titulo,
                        id_autor=self.id_autor,
                        fondo_cm=self.fondo_cm,
                        ancho_cm=self.ancho_cm,
                        alto_cm=self.alto_cm,
                        tecnica=self.tecnica,
                        material_base=self.material_base,
                        material_secundario=self.material_secundario,
                        tematica=self.tematica,
                        id_usuario=self.id_usuario)


class ObraCreate(BaseModel):
    titulo: str 
    id_autor: int
    fondo_cm: int
    ancho_cm: int
    alto_cm: int
    tecnica: str | None
    material_base: str | None
    material_secundario: str | None
    tematica: str | None
    id_usuario: int

    def toDB(self) -> ObraDB:
        return ObraDB(titulo=self.titulo,
                        id_autor=self.id_autor,
                        fondo_cm=self.fondo_cm,
                        ancho_cm=self.ancho_cm,
                        alto_cm=self.alto_cm,
                        tecnica=self.tecnica,
                        material_base=self.material_base,
                        material_secundario=self.material_secundario,
                        tematica=self.tematica,
                        id_usuario=self.id_usuario)
