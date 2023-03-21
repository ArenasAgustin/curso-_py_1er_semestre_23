def doble(x):
  return x * 2
 
mi_lista = [1, 2, 3, 4, 5, 6]
mi_lista_2 = [18, -3, 5, 0, -1, 12]

lista_nueva = list(map(doble, mi_lista))

# Una función lambda se define donde se usa
lista_nueva_lambda = list(map(lambda x: x * 2, mi_lista)) 
lista_nueva_2 = list(filter(lambda x: x > 0, mi_lista))

print(lista_nueva) # [2, 4, 6, 8, 10, 12]
print(lista_nueva_lambda) # [2, 4, 6, 8, 10, 12]
print(lista_nueva_2) # [18, 5, 12]