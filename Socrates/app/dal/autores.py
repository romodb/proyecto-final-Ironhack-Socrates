from app.ajustes.settings import DB_CONNECTION, DB_NAME, DB_USER, DB_PORT, DB_HOST
from fastapi import HTTPException
from app.ajustes.settings import DB_NAME, DB_AUTORES

# Aquí debemos poner las queries que se van a realizar en la capa de los routers:
# Para haxcer un get:
def obtener_autores_id(id: int):
    connection = None
    try:
        connection = DB_CONNECTION
        cursor = connection.cursor(dictionary=True)  # Obtener resultados como diccionarios
        query = "SELECT id, nombre FROM autores_murcia"
        cursor.execute(query)
        autores = cursor.fetchall()  # Obtener todos los resultados
        return autores
    except Error as e:
        print(f"Error al obtener los autores: {e}")
        return []

# Hacemos el get pero con nombre: 
def obtener_autores_nombre():
    connection = None
    try:
        connection = DB_CONNECTION
        cursor = connection.cursor(dictionary=True)  # Obtener resultados como diccionarios
        query = "SELECT id, nombre FROM autores_murcia"
        cursor.execute(query)
        usuarios = cursor.fetchall()  # Obtener todos los resultados
        return usuarios
    except Error as e:
        print(f"Error al obtener a los autores: {e}")
        return []
    
# Función para crear un nuevo usuario (post), query:
def crear_autor(db: Session, nombre_autor: str, id_autor: int):
    db_autores = Usuario(nombre=nombre_autor, id=id_autor)
    db.add(db_autores)  # Agregar el usuario a la sesión
    db.commit()  # Guardar los cambios en la base de datos
    db.refresh(db_autores)  # Obtener los datos actualizados del usuario (incluyendo el ID generado)
    return db_autores

# Para actualizar usando put:
def actualizar_autores(db: Session, id_autor: int, nombre_autor: str):
    # Buscar el usuario por su ID
    db_autores = db.query(Usuario).filter(Usuario.id == id_autor).first()
    # Si el usuario no existe, devolver None:
    if db_autores is None:
        return None
    # Actualizar el nombre:
    db_autores.nombre = nombre_autor
    # Guardar los cambios en la base de datos:
    db.commit()
    db.refresh(db_autores)  # Refrescar los datos del usuario
    return db_autores

# Función para eliminar un usuario de la base de datos (delete):
def eliminar_autores(db: Session, id_autor: int):
    # Buscar al usuario por su ID
    db_autores = db.query(Usuario).filter(Usuario.id == id_autor).first()
    # Si el usuario no existe, devolver None
    if db_autores is None:
        return None
    # Eliminar el usuario de la base de datos
    db.delete(db_autores)
    db.commit()  # Guardar los cambios en la base de datos
    return db_autores


