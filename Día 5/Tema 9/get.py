from fastapi import FastAPI

app = FastAPI()

lista_de_productos = ['Producto 1', 'Producto 2', 'Producto 3']

@app.get("/")
async def root():
    '''
    Método que se ejecuta en la raiz del sitio
    @param Ninguno
    @return mensaje de bienvenida
    '''
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    '''
    Método que se ejecuta en /items/{item_id}
    @param item_id: int
    @return dict con el producto solicitado
    '''
    return {"item_id": item_id, "item": lista_de_productos[item_id]}