from models.usuarios import UsuarioDB as Usuario
from sqlalchemy.orm import sessionmaker
from settings.settings import engine


class UserDAO:
    def obtener_usuario_por_id(id: int) -> Usuario:
        Session = sessionmaker(bind=engine, autoflush=True)
        Session = Session()
        res = Session.get(Usuario, id)
        Session.close()
        return res
