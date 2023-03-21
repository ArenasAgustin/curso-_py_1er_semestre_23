"""
def multiplicar_por(x):
  def temp (n):
    return x*n
  return temp
"""

def multiplicar_por (n):
  return lambda x: x * n
  
duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)

print(duplicar(6)) # 12
print(triplicar(5)) # 15
print(diez_veces(12)) # 120