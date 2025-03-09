# Decorador (@), def (cabecera funcion con un pass), defines la variabe, 
# seleccionas el texto y haces docstring (""" """)

from fastapi import APIRouter, JSONResponse
from app.dal.autores import actualizar_autores, crear_autor, obtener_autores_id, eliminar_autores, obtener_autores_nom
# from app.dal.autores import 
router = APIRouter(prefix='/autores')

# Con autores los endpoint´s a desarollar son los siguientes:

@router.get('/id_autor/{id}')
async def new_data(id: int):
    """Usando el id de un autor va a buscarlo en la db y va a devolver su nombre completo.

    Args:
        datos_ls (list[int]): un id que identifique a un autor
    Returns:
         el nombre del autor
    """
    autores = obtener_autores_nom()  # Llamada a la función DAO
    if autores:
        return JSONResponse(content=autores, status_code=200)  # Respuesta con lista de autores
    else:
        return JSONResponse(content={"mensaje": "No se encontraron autores"}, status_code=404)  # Si no hay autores



@router.get('/nombre_autor/{nombre}')
async def new_data(nombre: str):
    """Usando el nombre de un autor va a buscarlo en la db y va a devolver su id.

    Args:
        datos_ls (list[str]): nombre que identifique a un autor
    Returns:
         el id del autor
    """
    autores = obtener_autores_id()  # Llamada a la función DAO
    if autores:
        return JSONResponse(content=autores, status_code=200)  # Respuesta con lista de autores
    else:
        return JSONResponse(content={"mensaje": "No se encontraron autores"}, status_code=404)  # Si no hay autores
 
#  1º debes generar la estructura de la funcion, 2º añades un comentario de que hace,
#  3º completas la funcion y 4º aplicas el dicstring(""" """)
# async def new_data2(datos_ls: list[str]):
#     """Este endpoint da de alta a un nuevo autor.

#     Args:
#         datos_ls (list[str]): los distintos campos de un autor

#     Returns:
#         lista: los campos del autor creado, con el id de sql
#     """
#     return datos_ls


# Put
@router.put('/change_data/{nombre}')
async def change_data(nombre: str):
    """Este endpoint modifica los datos de un autor.

    Args:
        datos_ls (list[str]): los distintos campos de un autor

    Returns:
        lista: los campos del autor creado, con el id de sql
    """
    # Buscar el usuario por su ID
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    # Si el usuario no existe, devolver None
    if db_usuario is None:
        return None
    # Actualizar los campos
    db_usuario.nombre = nombre
    db_usuario.email = email
    # Guardar los cambios en la base de datos
    db.commit()
    db.refresh(db_usuario)  # Refrescar los datos del usuario
    return db_usuario



# Post, DEBES REVISARLO.
@router.post('/create_data/{nuevo_nombre}')
async def change_data(nombre: str):
    """Este endpoint añade datos a la db de los datos de un autor.

    Args:
        datos_ls (list[str]): el nombre de un autor nuevo.

    Returns:
        lista: el id del nuevo autor.
    """
        # Verificar si el id ya existe
    db_usuario = db.query(Usuario).filter(Usuario.id_autor == usuario.id_autor).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso")
    # Llamar a la función para crear el usuario
    nuevo_usuario = crear_usuario(db=db, nombre=usuario.nombre, email=usuario.email)
    return nuevo_usuario
    
    


@router.delete('/delete/{id}')
async def detel_data(id: int):
    """Este endpoint elimina los datos de un autor buscandolo por su id.

    Args:
        datos_ls (list[str]): el id de un autor.

    Returns:
        lista: de los valores borrados, emitira un codigo de error si no localiza el id.
    """
    # Llamar a la función para eliminar el usuario
    usuario_eliminado_id = eliminar_usuario(db=db, usuario_id=usuario_id)
    # Si no se encuentra el usuario, lanzar una excepción 404
    if usuario_eliminado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_eliminado




@router.delete('/delete/{nombre}')
async def detel_data(nombre: str):
    """Este endpoint elimina los datos de un autor pero buscandolo por su nombre.

    Args:
        datos_ls (list[str]): el nombre de un autor.

    Returns:
        lista: de los valores borrados, emitira un codigo de error si no localiza el nombre.
    """
    # Llamar a la función para eliminar el usuario
    usuario_eliminado_nombre = eliminar_usuario(db=db, usuario_id=usuario_id)
    # Si no se encuentra el usuario, lanzar una excepción 404
    if usuario_eliminado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_eliminado
