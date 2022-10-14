from httpx import get
import pytest

def test_fazer_requisicao():
    requisicao = get('http://127.0.0.1:8000/item/foo?obrigatorio=yes&skip=0&limit=2')
    requisicao_to_json = requisicao.json()
    print(requisicao_to_json)
