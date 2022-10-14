from fastapi import FastAPI

app = FastAPI()

fakes_items = [{'item_name': 'foo'}, {'item_name': 'bar'}, {'item_name': 'baz'}]


@app.get('/items/')
async def ler_nome_dos_items(skip: int = 0, limit: int = 0):
    return fakes_items[skip: skip + limit]


# parâmetro de consulta opcional python 3.10
@app.get('/items/{item_id}')
async def parametro_de_consulta_opcional(item_id: str, query: str | None = None, short: bool = False):
    item = {'item_id': item_id}
    if query:
        return {'item_id': item_id, 'query': query}

    if not short:
        item.update(
            {'descricao': 'Isso é um item com uma descrição bem grandona mesmo'}
        )

    return item


#  roda com múltiplos parâmetro de consulta
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, query: str | None = None, short: bool = False):
    item = {'item_id': item_id, 'user_id': user_id}
    if query:
        item.update({'query': query})
    if not short:
        item.update({
            'item_id': 'É um produto com uma descrição bem grandona mesmo'
        })

    return item


#  parâmetro de consulta obrigatório
@app.get('/item/{item_id}')
async def parametro_obrigatorio(item_id: str, obrigatorio: str, skip: int, limit: int | None = None):
    return {'item_id': item_id, 'obrigatorio': obrigatorio, 'skip': skip, 'limit': limit}
