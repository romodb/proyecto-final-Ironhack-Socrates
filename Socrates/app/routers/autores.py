# Decorador (@), def (cabecera funcion con un pass), defines la variabe, 
# seleccionas el texto y haces docstring (""" """)
from fastapi import APIRouter, HTTPException, Response, status
from dal.autores import obtener_autor_por_id, obtener_autores_nombre, eliminar_autores


# from app.dal.autores import 
autor_router = APIRouter(prefix='/autores')

# Con autores los endpoint´s a desarollar son los siguientes:

@autor_router.get('/id_autor/{id}')
async def get_by_id(id: int):
    """Usando el id de un autor va a buscarlo en la db y va a devolver su nombre completo.

    Args:
        datos_ls (list[int]): un id que identifique a un autor
    Returns:
         el nombre del autor
    """
    autor = obtener_autor_por_id(id)  # Llamada a la función DAO
    if autor:
        # return Response(content=autor, status_code=status.HTTP_200_OK)  # Respuesta con lista de autores
        return autor
    else:
        raise HTTPException(detail={"mensaje": f"No se encontró al autor con id {id}"}, status_code=status.HTTP_404_NOT_FOUND)  # Si no hay autores


# Version hecha por nassh y que deberias imitar ;~;
# @autor_router.get('/{id}')
# async def get_by_id_2(id: int):
#     """_summary_

#     Args:
#         id (int): _description_

#     Raises:
#         HTTPException: _description_

#     Returns:
#         _type_: _description_
#     """
#     autor = obtener_autores_id(id)
#     if autor == None: 
#         raise HTTPException(detail={"mensaje": "No se encontraron autores"}, status_code=404)  # Si no hay autores
#     return Response(content=autor, status_code=status.HTTP_200_OK)


@autor_router.get('/nombre_autor/{nombre_autor}')
async def get_by_name(nombre_autor: str):
    """Usando el nombre de un autor va a buscarlo en la db y va a devolver su id.

    Args:
        datos_ls (list[str]): nombre que identifique a un autor
    Returns:
         el id del autor
    """
    autores = obtener_autores_nombre(nombre_autor)  # Llamada a la función DAO
    if autores:
        return autores
        # return Response(content=autores, status_code=status.HTTP_200_OK)  # Respuesta con lista de autores
    else:
        raise HTTPException(detail={"mensaje": "No se encontraron autores"}, status_code=status.HTTP_404_NOT_FOUND)  # Si no hay autores
 
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
@autor_router.put('/change_data/{nombre_autor}')
async def change_data(nombre: str):
    """Este endpoint modifica los datos de un autor.

    Args:
        datos_ls (list[str]): los distintos campos de un autor

    Returns:
        lista: los campos del autor creado, con el id de sql
    """
    pass


# Post, DEBES REVISARLO.
@autor_router.post('/create_data/{nuevo_nombre}')
async def change_data(nombre_autor: str):
    """Este endpoint añade datos a la db de los datos de un autor.

    Args:
        datos_ls (list[str]): el nombre de un autor nuevo.

    Returns:
        lista: el id del nuevo autor.
    """
        # Verificar si el id ya existe
    # if crear_autor == True:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El valor que has puesto no es válido, revisa que es un nombre.")
    # Llamar a la función para crear el usuario
    # nuevo_usuario = crear_autor(db=DB_AUTORES, nombre=nombre_autor.nombre)
    # return nuevo_usuario
    pass
    
    


@autor_router.delete('/delete/{id_autor}')
async def detele_by_id(id: int):
    """Este endpoint eliminara todos los datos de un autor buscandolo por su id.

    Args:
        (id_autor: int, nombre_autor: str): el id de un autor.

    Returns:
        lista: de los valores borrados, emitira un codigo de error si no localiza el id.
    """
    # Llamar a la función para eliminar el usuario

    num_eliminados = eliminar_autores(id)
    if num_eliminados == 0:
        raise HTTPException(detail='No se han eliminado autores por que no se han encontrado por su id', status_code=status.HTTP_404_NOT_FOUND)
    return f'Se han eliminado {num_eliminados} autores.'

