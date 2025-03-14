from fastapi import APIRouter, Response, HTTPException, status
from dal.obras_arte import ObraDAO
from dal.autores import AutorDAO
from dal.usuarios import UserDAO
from models.obras_arte import ObraRead, ObraCreate

obras_arte_router = APIRouter(prefix='/obras')


@obras_arte_router.get('/', response_model=list[ObraRead], status_code=status.HTTP_200_OK)
async def obtnener_obras(limit: int = 50, offset: int = 0) -> list[ObraRead]:
    """Devuelve las últimas obras en el sistema según el limit y el offset

    Args:
        limit (int, optional): Cantidad máximo de obras a mostrar. Valor máximo 200. Defaults to 50.
        offset (int, optional): Desplazamiento de las obras. Defaults to 0.

    Returns:
        list[ObraRead]: listado de las obras
    """
    limit = 200 if limit > 200 else 50 if limit < 0 else limit
    obras = [obra.as_base_model() for obra in ObraDAO.get_obras(limit, offset)]
    return obras


@obras_arte_router.get('/{id}', response_model=ObraRead, status_code=status.HTTP_200_OK)
async def obtener_obra(id: int) -> ObraRead:
    """Dado un id de obra, devuelve la obra en cuestión

    Args:
        id (int): el id que es la clave primaria  de la obra

    Raises:
        HTTPException: Error 404 si la obra no eixte

    Returns:
        ObraRead: La obra en cuestión
    """
    obra = ObraDAO.get_obra(id)
    if not obra:
        raise HTTPException(detail=f'No existe obra con el id {id}', status_code=status.HTTP_404_NOT_FOUND)
    return obra.as_base_model()


@obras_arte_router.post('/', response_model=ObraRead, status_code=status.HTTP_200_OK)
async def create_obra(new_obra: ObraCreate) -> ObraRead:
    """Crear una nueva obra según el modelo ObraCreate. Aplica validaciones a los campos informados

    Args:
        new_obra (ObraCreate): estructura de la nueva obra

    Returns:
        ObraRead: La obra creada con su nuevo identificador
    """
    if not AutorDAO.obtener_autor_por_id(new_obra.id_autor):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'El autor con el id {new_obra.id_autor} no existe')
    if not UserDAO.obtener_usuario_por_id(new_obra.id_usuario):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'El usuario con el id {new_obra.id_usuario} no existe')
    obra = ObraDAO.create_obra(new_obra)
    return obra.as_base_model()



@obras_arte_router.delete('/', status_code=status.HTTP_202_ACCEPTED)
async def delete_obra(id: int) -> Response:
    """Dado el id de una obra procede a borrarla

    Args:
        id (int): id de la obra a borrar

    Raises:
        HTTPException: Error 404 si la obra no eixte

    Returns:
        Reponse
    """
    if not ObraDAO.get_obra(id): raise HTTPException(detail=f'No existe la obra {id}', status_code=status.HTTP_404_NOT_FOUND)
    eliminadas = ObraDAO.eliminar_obra(id)
    return Response(content=f'Se han eliminado {eliminadas} {'obra' if eliminadas == 1 else 'obra'}.')
