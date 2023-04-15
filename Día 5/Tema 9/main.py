from typing import Union
from fastapi import FastAPI

app = FastAPI()

listaDeProductos = {}

@app.get("/")
def read_root():
    '''
    Método que se ejecuta en la raiz del sitio
    @param Ninguno
    @return dict con el mensaje de bienvenida
    '''
    return {"Hello": "World"}


@app.get("/items")
def read_items():
    '''
    Método que se ejecuta en /items
    @param Ninguno
    @return lista de productos
    '''
    return listaDeProductos


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @param q: str
    @return el producto solicitado
    '''
    if item_id in listaDeProductos:
        return {"item": listaDeProductos[item_id], "q": q}
    else:
        return {"Error": "Producto no encontrado"}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @param item: Item
    @return dict con el producto creado
    '''
    listaDeProductos[item_id] = item
    return {"item": listaDeProductos[item_id]}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @param item: Item
    @return dict con el producto actualizado
    '''
    if item_id in listaDeProductos:
        listaDeProductos[item_id] = item
        return {"item": listaDeProductos[item_id]}
    else:
        return {"Error": "Producto no encontrado"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @return el producto eliminado
    '''
    if item_id in listaDeProductos:
        item = listaDeProductos[item_id]
        listaDeProductos.pop(item_id)
        return {"item": item}
    else:
        return {"Error": "Producto no encontrado"}


@app.get("/bye")
def read_root():
    '''
    Método que se ejecuta en /bye
    @param Ninguno
    @return dict con el mensaje de despedida
    '''
    return {"Bye": "World"}
