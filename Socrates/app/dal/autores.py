from ajustes.settings import engine
from models.autores import Autor
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Aquí debemos poner las queries que se van a realizar en la capa de los routers:
# Para haxcer un get:
def obtener_autor_por_id(id: int) -> dict[int, str]:
        Session = sessionmaker(bind=engine, autoflush=True)
        Session = Session()
        res = Session.get(Autor, id)
        Session.close()
        return res
    

# Hacemos el get pero con nombre: 
def obtener_autores_nombre(nombre: str):
    Session = sessionmaker(bind=engine,autoflush=False)
    return Session().query(Autor).filter(Autor.nombre_autor.like(f'%{nombre}%')).all()
    
# Función para crear un nuevo usuario (post), query:
def crear_autor(db, nombre_autor: str):
    db_usuario = Session.query(autores).filter(autores.nombre_autor == nombre_autor).first()

    db_autores = autores(nombre=nombre_autor)
    db.add(db_autores)  # Agregar el usuario a la sesión
    db.commit()  # Guardar los cambios en la base de datos
    db.refresh(db_autores)  # Obtener los datos actualizados del usuario (incluyendo el ID generado)
    return db_autores

# Para actualizar usando put:
def actualizar_autores(db, nombre_autor: str):
    # Buscar el usuario por su ID
    # db_autores = DB_NAME.query(autores).filter(autores.id == id_autor).first()
    # # Si el usuario no existe, devolver None:
    # if db_autores is None:
    #     return None
    # # Actualizar el nombre:
    # db_autores.nombre = nombre_autor
    # # Guardar los cambios en la base de datos:
    # db.commit()
    # db.refresh(db_autores)  # Refrescar los datos del usuario
    return db_autores

# Función para eliminar un usuario de la base de datos (delete):
def eliminar_autores(id: int):
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
    


