def tratarModificarLista(lista):
    print('Obtuve', lista)
    lista.append(4)
    print('Ahora es', lista)


listaOriginal = list(range(3))
print('Previo a llamarse', listaOriginal)
tratarModificarLista(listaOriginal)
print('Luego de modificarse', listaOriginal)


def usamosParametro(lista):
    print('Obtuve', lista)
    lista = list(range(5))
    print('Ahora es', lista)
    print('Ahora es', listaOriginal)


listaOriginal = list(range(3))
print('Previo a llamarse', listaOriginal)
usamosParametro(listaOriginal)
print('Luego de modificarse', listaOriginal)
