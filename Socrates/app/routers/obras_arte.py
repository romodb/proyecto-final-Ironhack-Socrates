from fastapi import APIRouter
# from app.dal.usuarios import 
router = APIRouter(prefix='/usuarios')

# Con usuarios los endpoint´s a desarollar son los siguientes:

@router.get('/id_usuarios/{id}')
async def new_data(id: int):
    """Read: 
    Recoge los valores que cumplan un requisito
    Te devuelve los valores que cumplan un requisito"""

    pass

@router.get('/nombre_usuarios/{nombre}')
async def new_data(nombre: str):
    """Read: 
    Recoge los valores que cumplan un requisito
    Te devuelve los valores que cumplan un requisito"""

    pass

#  1º debes generar la estructura de la funcion, 2º añades un comentario de que hace,
#  3º completas la funcion y 4º aplicas el dicstring(""" """)
async def new_data2(datos_ls: list[str]):
    """Este dnspoint da de alta a un nuevo usuarios.

    Args:
        datos_ls (list[str]): los distintos campos de un usuarios

    Returns:
        lista: los campos del usuarios creado, con el id de sql
    """
    return datos_ls


@router.put('/change_data')
async def change_data():
    """Replace: mofica datos de usuarioses:
    Recoge un nombre de un usuarios o su id para identificarlo y modificarlo
    Devuelve los datos tras cambiarlo
    """
    pass


@router.post('/create_data')
async def change_data():
    """Create: dar de alta a usuarioses:
    Recoge un nuevo nombre.
    Devuelve el id de este nuevo usuarios"""
    pass

@router.delete('/delete')
async def detel_data():
    """Delete: borra valores con una caracteristica concreta.
    Recoge un nombre o un id
    Devuelve un recuento con el numero de valores que cumplan ese requisito y que hayan sido borrados."""
    pass 