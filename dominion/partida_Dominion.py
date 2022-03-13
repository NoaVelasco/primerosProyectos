from random import randint

tuplaCartas = (
    "Capilla",
    "Foso",
    "Sótano",
    "Aldea",
    "Canciller",
    "Leñadores",
    "Taller",
    "Banquete",
    "Burócrata",
    "Espía",
    "Herrería",
    "Jardines",
    "Ladrón",
    "Milicia",
    "Prestamista",
    "Remodelar",
    "Salón del Trono",
    "Biblioteca",
    "Bruja",
    "Festival",
    "Laboratorio",
    "Mercado",
    "Mina",
    "Sala del Consejo",
    "Aventurero"
)

listaCartas = list(tuplaCartas)
numCartas = 0
while numCartas < 10:
    indexrand = randint(0, int(len(listaCartas)))
    print(listaCartas[indexrand])
    listaCartas.pop(indexrand)
    numCartas += 1
