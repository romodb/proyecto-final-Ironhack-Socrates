from fastapi import APIRouter, HTTPException, Response, status
from dal.autores import AutorDAO
from dal.obras_arte import ObraDAO
from models.autores import AutorRead, AutorCreate


autor_router = APIRouter(prefix='/autores')


@autor_router.get('/{id}', response_model=AutorRead, status_code=status.HTTP_200_OK)
async def get_by_id(id: int) -> AutorRead:
    """Dado el id de un autor devuelve el objeto autor según el Modelo Autor

    Args:
        id (int): El id que es la clave primaria del autor

    Raises:
        HTTPException: Si no existe autor con el id especificado
        devuelve un error HTTP 404.

    Returns:
        Autor: Objeto Autor según el modelo
    """
    autor = AutorDAO.obtener_autor_por_id(id)
    if not autor:
        raise HTTPException(detail={"mensaje": f"No se encontró al autor con id {id}"}, status_code=status.HTTP_404_NOT_FOUND)
    return autor.as_base_model()


@autor_router.get('/nombre/{nombre_autor}', response_model=list[AutorRead], status_code=status.HTTP_200_OK)
async def search_autor(nombre_autor: str) -> list[AutorRead]:
    """Dado el nombre de un autor devuelve una lista con todos los autores que contengan el nombre especificado

    Args:
        nombre_autor (str): nombre del autor

    Raises:
        HTTPException: Si no se encuentra ningún autor el sistema devuelve un error 404

    Returns:
        list[AutorRead]: lista con los autores con el nombre especificado
    """
    autores = AutorDAO.obtener_autores_nombre(nombre_autor)
    if len(autores) == 0:
        raise HTTPException(detail={"mensaje": f"No se encontraron autores con el nombre {nombre_autor}"}, status_code=status.HTTP_404_NOT_FOUND)
    return [autor.as_base_model() for autor in autores]
 

@autor_router.post('/', response_model=AutorRead, status_code=status.HTTP_201_CREATED)
async def create_autor(new_autor: AutorCreate) -> AutorRead:
    """Este endpoint añade datos a la db un nuevo autor.

    Args:
        datos_ls (list[str]): el nombre de un autor nuevo.

    Returns:
        lista: el id del nuevo autor.
    """
    autor = AutorDAO.crear_autor(new_autor.nombre)
    if not autor:
        raise HTTPException(detail={"message":f"El autor {new_autor.nombre} ya existe en la base de datos"}, status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return autor.as_base_model()


@autor_router.delete('/{id_autor}', status_code=status.HTTP_202_ACCEPTED)
async def detele_autor(id: int) -> Response:
    """Este endpoint eliminara todos los datos de un autor buscandolo por su id.

    Args:
        (id_autor: int, nombre_autor: str): el id de un autor.

    Returns:
        lista: de los valores borrados, emitira un codigo de error si no localiza el id.
    """
    if not AutorDAO.obtener_autor_por_id(id):
        raise HTTPException(detail=f'No existen autores por el id {id}', status_code=status.HTTP_404_NOT_FOUND)
    if ObraDAO.get_obras_autor(id):    
        raise HTTPException(detail=f'No se puede elimiar el autor con id {id} debido a que que tiene obras asignadas', status_code=status.HTTP_406_NOT_ACCEPTABLE)        
    num_eliminados = AutorDAO.eliminar_autores(id)
    return Response(content=f'Se han eliminado {num_eliminados} autores.', status_code=status.HTTP_202_ACCEPTED)
