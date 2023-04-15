from fastapi import FastAPI

app = FastAPI()

lista_de_productos = [{'nombre': 'Producto 1', 'precio': 100}, 
                      {'nombre': 'Producto 2', 'precio': 200}, 
                      {'nombre': 'Producto 3', 'precio': 300}]

@app.post("/items")
async def create_item(item: Item):
    '''
    Método que se ejecuta en /items
    @param item: Item
    @return lista con todos los elemetos
    '''
    lista_de_productos.append(item)
    return {"list": lista_de_productos}