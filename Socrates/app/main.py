from fastapi import FastAPI, HTTPException, Response, status
from fastapi.responses import RedirectResponse
from app.ajustes.settings import DEV, APP_HOST, APP_PORT
from app.routers.autores import router as router_autores 
from app.routers.usuarios import router as router_usuario 
from app.routers.obras_arte import router as router_obras_arte 
import uvicorn

# Iniciamos el proceso:
socrates = FastAPI()
socrates.add_api_route(router_autores)
socrates.add_api_route(router_usuario)
socrates.add_api_route(router_obras_arte)




# Esto ejecuta el código de la api:
if __name__ == '__main__':
    uvicorn.run(app='main:socrates', host=APP_HOST, port=APP_PORT, reload=DEV)
