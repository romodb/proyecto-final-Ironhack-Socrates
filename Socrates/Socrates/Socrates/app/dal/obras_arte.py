from sqlalchemy.orm import sessionmaker
from models.obras_arte import ObraCreate, ObraDB as Obra
from settings.settings import engine

class ObraDAO:

    def get_obras(limit: int = 200, offset: int = 0) -> list[Obra]:
        Session = sessionmaker(bind=engine, autoflush=True)
        obras = Session().query(Obra).limit(limit).offset(offset).all()
        return obras


    def get_obra(id: int) -> Obra:
        Session = sessionmaker(bind=engine, autoflush=True)
        Session = Session()
        obra = Session.get(Obra, id)
        Session.close()
        return obra
    

    def get_obras_autor(id_autor) -> list[Obra]:
        Session = sessionmaker(bind=engine, autoflush=True)
        obras = Session().query(Obra).filter(Obra.id_autor==id_autor).all()
        return obras


    def create_obra(new_obra: ObraCreate):
        obra = new_obra.toDB()
        Session = sessionmaker(bind=engine,autoflush=True)
        Session = Session()
        Session.add(obra)
        print(obra)
        Session.commit()
        Session.refresh(obra)
        return obra


    def eliminar_obra(id: int) -> int:
        Session = sessionmaker(bind=engine, autoflush=True)
        Session = Session()
        obra = Session.get(Obra, id)
        if obra:
            Session.delete(obra)
            Session.commit()
            Session.close()
            return 1
        else:
            return 0
