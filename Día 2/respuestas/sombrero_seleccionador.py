import time

coraje = 0
orgullo = 0
inteligencia = 0
responsabilidad = 0
amistad = 0
pureza = ""
casa_no_deseada = ""

print("\nAsi que tengo que elegir a que casa vas, muy bien empecemos...")

while True:
    coraje = int(input("\nVeo que tienes un coraje de (desde 1 al 10): "))
    if coraje >= 1 and coraje <= 10:
        break

while True:
    orgullo = int(input("\nTu nivel de orgullo es de (desde 1 al 10): "))
    if orgullo >= 1 and orgullo <= 10:
        break

while True:
    inteligencia = int(
        input("\nLa inteligencia que tienes es de (desde 1 al 10): "))
    if inteligencia >= 1 and inteligencia <= 10:
        break

while True:
    responsabilidad = int(
        input("\nVeamos que tan responsable eres (desde 1 al 10): "))
    if responsabilidad >= 1 and responsabilidad <= 10:
        break

while True:
    amistad = int(input("\nQue tan amistoso/a sos (desde 1 al 10): "))
    if amistad >= 1 and amistad <= 10:
        break

while True:
    pureza = input("\nEres de sangre pura o mestiza? (puro o mestizo): ").lower()
    if pureza == "puro" or pureza == "mestizo":
        break

while True:
    casa_no_deseada = input(
        "\nY por último, a donde NO quieres ir? (Gryffindor, Slytherin, Hufflepuff, Ravenclaw): ").lower()
    if casa_no_deseada == "gryffindor" or casa_no_deseada == "slytherin" or casa_no_deseada == "hufflepuff" or casa_no_deseada == "ravenclaw":
        break

print("\nEstoy pensando.. \n")
time.sleep(2)
print("\nEstoy pensando... \n")
time.sleep(2)

if coraje >= 8 and casa_no_deseada != "gryffindor":
    print("\nGRYFFINDOR!!!")

elif orgullo >= 8 and inteligencia >= 8 and pureza == "puro" and casa_no_deseada != "slytherin":
    print("\nSLYTHERIN!!!")

elif responsabilidad >= 8 and inteligencia >= 8 and casa_no_deseada != "ravenclaw":
    print("\nRAVENCLAW!!!")

elif amistad >= 8 and casa_no_deseada != "hufflepuff":
    print("\nHUFFLEPUFF!!!")

else:
    print("\nERES UN NO MAGO!!!")
