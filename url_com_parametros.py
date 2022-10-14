from fastapi import FastAPI
from enum import Enum


class ModeloNomes(str, Enum):
    joao = 'Joao'
    rafa = 'Rafael'
    lucas = 'Lucas'


app = FastAPI()


#  criando uma rota que contém uma rota como parâmetro
@app.get('/files/{file_path:path}')
async def get_rota_dentro_da_rota(file_path: str):
    return {'file_path': file_path}


@app.get('/modelos/{modelos}')
async def get_modelos(modelos: ModeloNomes):
    if modelos is ModeloNomes.joao:
        return {'modelo': modelos, 'message': 'Gosto de programar por programar'}

    return {'modelo': modelos, 'message': 'Modelo não encontrado'}

@app.get('/usuarios/me')
async def get_user_me():
    return {'user_id': 'current_user'}


@app.get('/usuarios/{user_id}')
async def get_user(user_id: str):
    return {'user_id': user_id,
            'user_name': 'Joao'}


@app.get("/items/{item_id}")
async def ler_item(item_id: int):
    return {'item_id': item_id}
