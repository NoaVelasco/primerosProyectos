#-----------TAREAS-------------------
# Queda como tarea terminar la calculadora, para lo cual
# la resta, la multiplicación, la división...
# y la coma decimal, que solo puede ser una y pasa a float.

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()

operacion = ""
resultado = 0

# -----------------PANTALLA------------------

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla,
                 font=("Courier Prime", 22))
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#b0e0e6", justify="right")

# ----------PULSACIONES TECLADO--------------

# Función para mostrar en pantalla lo que pulsamos


def numeroPulsado(num):

    global operacion

    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        # concatena los números en pantalla
        numeroPantalla.set(numeroPantalla.get() + num)

# --------------FUNCIÓN SUMA--------------


def suma(num):

    global operacion
    global resultado

    resultado += int(num)

    operacion = "suma"

    numeroPantalla.set(resultado)

# --------------FUNCIÓN el_resultado--------------


def el_resultado():

    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get()))

    resultado = 0

# -----------------FILA 1------------------


boton7 = Button(miFrame, text="7", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="÷", width=8, height=4, font=(18))
botonDiv.grid(row=2, column=4)

# -----------------FILA 2------------------

# Para evitar que cuando el código llegue aquí interprete que debe mostrar un número concreto,
# no podemos usar command=numeroPulsado("4"). Tenemos que usar una función anónima lambda.
boton4 = Button(miFrame, text="4", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="×", width=8, height=4, font=(18))
botonMult.grid(row=3, column=4)

# -----------------FILA 3------------------

boton1 = Button(miFrame, text="1", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRes = Button(miFrame, text="–", width=8, height=4, font=(18))
botonRes.grid(row=4, column=4)

# -----------------FILA 4------------------

botonComa = Button(miFrame, text=",", width=8, height=4,
                   font=(18), command=lambda: numeroPulsado(","))
botonComa.grid(row=5, column=1)
boton0 = Button(miFrame, text="0", width=8, height=4,
                font=(18), command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=8, height=4, font=(
    18), command=lambda: el_resultado())
botonIgual.grid(row=5, column=3)
botonSum = Button(miFrame, text="+", width=8, height=4,
                  font=(18), command=lambda: suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

raiz.mainloop()
