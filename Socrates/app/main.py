from fastapi import FastAPI
from ajustes.settings import DEV, APP_HOST, APP_PORT
from routers.autores import autor_router 
# from routers.usuarios import usuario_router
from routers.obras_arte import obras_arte_router 
import uvicorn


# Iniciamos el proceso:
socrates = FastAPI()
socrates.include_router(autor_router)
# socrates.include_router(usuario_router)
socrates.include_router(obras_arte_router)




# Esto ejecuta el código de la api:
if __name__ == '__main__':
    uvicorn.run(app='main:socrates', host=APP_HOST, port=APP_PORT, reload=DEV)
