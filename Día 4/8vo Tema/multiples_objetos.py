class Animales:
    def __init__(self, nombre, cantidad_patas, sonido):
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        self.sonido = sonido
    def getNombre(self):
        '''
        Devuelve el ombre del animal
        @param Ninguno
        @return nombre del animal
        '''
        return self.nombre
    def getCantidadPatas(self):
        '''
        Devuelve la cantidad de patas del animal
        @param Ninguno
        @return cantidad de patas del animal
        '''
        return self.cantidad_patas
    def getSonido(self):
        '''
        Devuelve el sonido del animal
        @param Ninguno
        @return sonido del animal
        '''
        return self.sonido
    def setNombre(self, nombre):
        '''
        Establece el nombre del animal
        @param Nuevo nombre
        @return Nada
        '''
        self.nombre = nombre
    def setCantidadPatas(self, cantidad_patas):
        '''
        Establece la cantidad de patas del animal
        @param Nueva cantidad de patas
        @return Nada
        '''
        self.cantidad_patas = cantidad_patas
    def setSonido(self, sonido):
        '''
        Establece el sonido del animal
        @param Nuevo sonido
        @return Nada
        '''
        self.sonido = sonido
    def __str__(self):
        '''
        Devuelve una cadena con los datos del animal
        @param Ninguno
        @return Cadena con los datos del animal
        '''
        return f'Nombre: {self.nombre} - Cantidad de patas: {self.cantidad_patas} - Sonido: {self.sonido}' # f-strings: formateo de cadenas desde Python 3.6
    def __eq__(self, otro_animal):
        '''
        Compara dos animales
        @param Otro animal
        @return True si son iguales, False si son diferentes
        '''
        return (self.nombre == otro_animal.nombre 
            and self.cantidad_patas == otro_animal.cantidad_patas 
            and self.sonido == otro_animal.sonido)

def main():
    animal_1 = Animales('Perro', 4, 'Guau')
    animal_2 = Animales('Gato', 4, 'Miau')
    animal_3 = Animales('Pájaro', 2, 'Pio')
    animal_4 = Animales('Vaca', 4, 'Muu')

    print(animal_1)
    print(animal_2)
    print(animal_3)
    print(animal_4)

    print(animal_1 == animal_2) # Llamada implícita a __eq__
    print(animal_1.__eq__(animal_4))
main()