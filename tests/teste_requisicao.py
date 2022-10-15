from httpx import get
import pytest

def test_fazer_requisicao():
    requisicao = get('http://127.0.0.1:8000/item/foo?obrigatorio=yes&skip=0&limit=2')
    requisicao_to_json = requisicao.json()
    print(requisicao_to_json)


def test_iterar_lista_dicionario():
    lista_dict = [{'chave': 'valor'}, {'chave2': 1}]

    for i in lista_dict:
        print(i)