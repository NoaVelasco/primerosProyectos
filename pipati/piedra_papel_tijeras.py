# Noa Velasco 20220225
# Rock, Paper, Scissors (spa)
# My first game

from random import randint # También se puede hacer con random.choice()
  
print("¿Te apetece jugar a piedra-papel-tijeras?")
print("Vale, pues a la de tres...:")
print("Piedra...")
print("Papel...")
print("¡Tijeras!")

piedra = "piedra"
papel = "papel"
tijeras = "tijeras"

# En el futuro, mi intención es prescindir de estas 3 variables y tirar de la siguiente lista:

opciones = [piedra, papel, tijeras]
userCont = 0
machinCont = 0

pptAlea = randint(0, 100)
if pptAlea < 40:
    machinInput = piedra
elif pptAlea > 75:
    machinInput = papel
else:
    machinInput = tijeras

# Reconozco que he hecho trampas. Se dice que la primera jugada tiende más a ser tijeras.

userElige = input(">>>")
userInput = userElige.lower()

while userInput not in opciones:
    print("Escríbelo otra vez, por favor.")
    userInput = input(">>>").lower()

print("Yo he elegido " + machinInput + ".")
print("Y tú has elegido " + userInput + ".")

if userInput != machinInput:
    if machinInput == piedra and userInput == papel:
        print("Has ganado")
        userCont += 1
    elif machinInput == piedra and userInput == tijeras:
        print("Has perdido")
        machinCont += 1
    elif machinInput == papel and userInput == tijeras:
        print("Has ganado")
        userCont += 1
    elif machinInput == papel and userInput == piedra:
        print("Has perdido")
        machinCont += 1
    elif machinInput == tijeras and userInput == piedra:
        print("Has ganado")
        userCont += 1
    elif machinInput == tijeras and userInput == papel:
        print("Has perdido")
        machinCont += 1
else:
    print("Empate")

# Cada cierto tiempo quiero darle una vuelta hasta lograr una forma más elegante.

print("Esto solo ha sido un calentamiento. \n¿Qué te parece? ¿Jugamos hasta que alguien supere al otro por dos?")

# Se puede hacer muy cansino. Tal vez lo cambie al primero que llegue a 3.

def partida():

    global userCont
    global machinCont

    print("Piedra...")
    print("Papel...")
    print("¡Tijeras!")

    pptAlea = randint(0, 2)
    if pptAlea == 0:
        machinInput = piedra
    elif pptAlea == 1:
        machinInput = papel
    else:
        machinInput = tijeras

    userElige = input("Elige: \n>>>")
    userInput = userElige.lower()
    
    while userInput not in opciones:
        print("Escríbelo otra vez, por favor.")
        userInput = input(">>>").lower()

    print("Yo he elegido " + machinInput + ".")
    print("Y tú has elegido " + userInput + ".")

    if userInput != machinInput:
        if machinInput == piedra and userInput == papel:
            print("Has ganado")
            userCont = userCont+1
            comprobante(machinCont, userCont)
        elif machinInput == piedra and userInput == tijeras:
            print("Has perdido")
            machinCont = machinCont+1
            comprobante(machinCont, userCont)
        elif machinInput == papel and userInput == tijeras:
            print("Has ganado")
            userCont = userCont+1
            comprobante(machinCont, userCont)
        elif machinInput == papel and userInput == piedra:
            print("Has perdido")
            machinCont = machinCont+1
            comprobante(machinCont, userCont)
        elif machinInput == tijeras and userInput == piedra:
            print("Has ganado")
            userCont = userCont+1
            comprobante(machinCont, userCont)
        elif machinInput == tijeras and userInput == papel:
            print("Has perdido")
            machinCont = machinCont+1
            comprobante(machinCont, userCont)
    else:
        print("Empate")
        comprobante(machinCont, userCont)


def comprobante(machinCont, userCont):
    print(f"Yo he ganado: {machinCont}.")
    print(f"Tú has ganado: {userCont}.")

    if abs(userCont - machinCont) != 2:
        partida()
    elif userCont == (machinCont + 2):
        print("Está bien, no hay quien pueda contigo.")
    elif machinCont == (userCont + 2):
        print("Has jugado bien. Para un ser humano, jijiji.")


partida()