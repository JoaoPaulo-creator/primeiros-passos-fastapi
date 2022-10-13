from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
async def ler_item(item_id: int):
    if item_id is not int:
        return 'Invalid id'
    return {'item_id': item_id}
