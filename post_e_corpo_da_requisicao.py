from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    nome_do_produto: str
    descricao: str | None = None
    preco: float
    taxa: float | None = None


app = FastAPI()

@app.post('/item')
async def criar_um_item(item: Item):
    # acessando os atributos do objeto Item
    item_dict = item.dict()
    if item.taxa:
        preco_com_taxa = item.preco + item.taxa
        item_dict.update({'preco_com_taxa': preco_com_taxa})

    return item_dict


# rota com parâmetros

@app.post('/items/{item_id}')
async def criar_item_rota_com_parametro(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}


#  parâmetro de rota + parâmetro de consulta
@app.post('/items/{item_id_}')
async def criar_item_rota_com_parametro_de_consulta(item_id_: int, item: Item, query: str | None = None):
    resultado = {'item_id': item_id_, **item.dict()}
    if query:
        resultado.update({'query': query})

    return resultado
