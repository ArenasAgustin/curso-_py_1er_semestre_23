from fastapi import FastAPI

app = FastAPI()

lista_de_productos = [{'nombre': 'Producto 1', 'precio': 100}, 
                      {'nombre': 'Producto 2', 'precio': 200}, 
                      {'nombre': 'Producto 3', 'precio': 300}]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @param item: Item
    @return item actualizado
    '''
    lista_de_productos[item_id] = item
    return {"item": lista_de_productos[item_id]}