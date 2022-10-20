from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.post("/cadastro")
async def get_dados_pessoa(primeiro_nome: str, segundo_nome: str | None = None, idade: int | None = None):
    return {
        'primeiro_nome': primeiro_nome,
        'segundo_nome': segundo_nome,
        'idade': idade
    }


@app.get("/cadastro/{primeiro_nome}")
async def foo(primeiro_nome: str):
    return {'primeiro_nome': primeiro_nome}
