from fastapi import FastAPI

app = FastAPI()

lista_de_productos = [{'nombre': 'Producto 1', 'precio': 100}, 
                      {'nombre': 'Producto 2', 'precio': 200}, 
                      {'nombre': 'Producto 3', 'precio': 300}]

@app.delete("/items/{item_id}")
async def update_item(item_id: int):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @return el producto eliminado
    '''
    return {"item": lista_de_productos.pop(item_id)}