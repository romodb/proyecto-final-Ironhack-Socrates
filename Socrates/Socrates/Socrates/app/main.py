from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from settings.settings import Settings
from routers.autores import autor_router 
from routers.usuarios import usuario_router
from routers.obras_arte import obras_arte_router 
import uvicorn


# Iniciamos el proceso:
socrates = FastAPI()
socrates.include_router(autor_router)
socrates.include_router(usuario_router)
socrates.include_router(obras_arte_router)


@socrates.get('/')
def redirect() -> RedirectResponse:
    return RedirectResponse(url='/docs', status_code=status.HTTP_303_SEE_OTHER)



if __name__ == '__main__':
    uvicorn.run(app='main:socrates', host=Settings().app_host, port=Settings().app_port, reload=Settings().dev_mode)
