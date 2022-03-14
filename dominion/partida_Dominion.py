# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

from random import randint


listaFija = [(2, 'Capilla'), (2, 'Foso'), (2, 'Sótano'), (3, 'Aldea'), (3, 'Canciller'), (3, 'Leñadores'), (3, 'Taller'), (4, 'Banquete'), (4, 'Burócrata'), (4, 'Espía'), (4, 'Herrería'), (4, 'Jardines'), (4, 'Ladrón'),
             (4, 'Milicia'), (4, 'Prestamista'), (4, 'Remodelar'), (4, 'Salón del Trono'), (5, 'Biblioteca'), (5, 'Bruja'), (5, 'Festival'), (5, 'Laboratorio'), (5, 'Mercado'), (5, 'Mina'), (5, 'Sala del Consejo'), (6, 'Aventurero')]

listaTemp = []
numCartas = 0

while numCartas < 10:
    indexrand = randint(0, int(24-len(listaTemp)))
    loteria = listaFija[indexrand]
    if loteria not in listaTemp:
        listaTemp.append(loteria)
        numCartas += 1

for x in sorted(listaTemp):
    print(x[0], "-", x[1])

#--------------¿CAMBIAMOS ALGUNA CARTA?---------------

print("------------------------")
cambio = input("¿Quieres cambiar alguna carta? \n s: sí / n: no \n>>>")

if cambio == "s":
    while(cambio == "s"):
        for x in sorted(listaTemp):
            print(f"[ {listaTemp.index(x)} ] _ {x[1]}")

        eliminar = int(
            input("¿Qué carta quito? Introduce su número de índice: "))
        print("------------------------")
        listaTemp.pop(eliminar)
        numCartas -= 1

        while numCartas < 10:
            indexrand = randint(0, int(24-len(listaTemp)))
            loteria = listaFija[indexrand]
            if loteria not in listaTemp:
                listaTemp.append(loteria)
                numCartas += 1

        for x in sorted(listaTemp):
            print(x[0], "-", x[1])

        cambio = input(
            "------------------------ \n¿Quieres cambiar alguna carta? \n s: sí / n: no \n>>>")

    print("------------------------ \n¡Disfruta de tu partida!")

elif cambio == "n":
    print("------------------------ \n¡Disfruta de tu partida!")

else:
    print("------------------------ \nNo te he entendido, así que voy a decir cartas al azar: \n s: sí / n: no \n>>>")
    aleatoria = input()

    while(aleatoria == "s"):
        print(listaFija[randint(0, 24)])
        aleatoria = input("------------------------ \n s: sí / n: no \n>>>")

    print("------------------------ \n¡Disfruta de tu partida!")
