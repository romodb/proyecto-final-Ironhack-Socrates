from settings.settings import engine
from models.autores import AutorDB as Autor
from sqlalchemy.orm import sessionmaker
from dal.obras_arte import ObraDAO

class AutorDAO:
    def obtener_autor_por_id(id: int) -> Autor:
        Session = sessionmaker(bind=engine, autoflush=True)
        Session = Session()
        res = Session.get(Autor, id)
        Session.close()
        return res


    def obtener_autores_nombre(nombre: str, perfect_matches = False) -> list[Autor]:
        Session = sessionmaker(bind=engine,autoflush=False)
        autores = Session().query(Autor).filter(Autor.nombre_autor.like(f'%{nombre.lower()}%')).all() if not perfect_matches else Session().query(Autor).filter(Autor.nombre_autor.like(f'{nombre.lower()}')).all()
        return autores


    def crear_autor(nombre: str) -> Autor:
        if len(ObraDAO.get_obras_autor(nombre)) == 0:
            autor = Autor(nombre_autor=nombre)
            Session = sessionmaker(bind=engine,autoflush=True)
            Session = Session()
            Session.add(autor)
            Session.commit()
            Session.refresh(autor)
            return autor
        else:
            return None


    def eliminar_autores(id: int) -> int:
        Session = sessionmaker(bind=engine,autoflush=True)
        Session = Session()
        autor = Session.get(Autor, id)
        if autor:
            Session.delete(autor)
            Session.commit()
            Session.close()
            return 1
        else:
            return 0
