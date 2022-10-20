from fastapi import FastAPI, Query
from typing import List, Union

app = FastAPI()

#  O None = None indica que o parâmetro não é obrigatório
#  Implementado uma validação adicional com Query

#  q: Union[str, None] = Query(default=None), torna o parâmetro opcional assim como q: str | None = None
@app.get('/items/')
async def pegar_itens(query: str | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")):

    '''

    Essa expressão regular específica verifica se o valor recebido no parâmetro:

    ^: Inicia com os seguintes caracteres, ou seja, não contém caracteres anteriores.
    fixedquery: contém o valor exato fixedquery.
    $: termina aqui, não contém nenhum caractere após fixedquery.
    '''

    resultado = {'itens': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if query:
        resultado.update({'query': query})

    return resultado

@app.get("/items-com-varios-parametros/")
async def itens_com_multiplos_parametros(query: Union[List[str], None] = Query(default=None)):
    query_items = {"query": query}
    return query_items


@app.get("/usando-list-inves-de-List/")
async def read_items(q: list = Query(default=[])):
    '''
    Usando list, o resultado final é o mesmo que usar List[str]\n
    '''
    query_items = {"q": q}
    return query_items