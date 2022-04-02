# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco. 
# CRUD v.2.220317.2

# Este CRUD forma parte de un ejercicio de Píldoras Informáticas.

import sqlite3
from tkinter import *
from tkinter import messagebox as msg

root = Tk()

root.option_add('*tearOff', FALSE)


miFrame = Frame(root, width=400, height=600, bg="moccasin")
miFrame.pack()

miFrameCRUD = Frame(root, width=400, height=600)
miFrameCRUD.pack()

inputSQL=[]
selectID = StringVar()
selectNom = StringVar()
selectApe = StringVar()
selectPass = StringVar()
selectDir = StringVar()

#-------------------MENU-------------------------------------
#__________CONEXION___________
class Conexion:

    def __init__(self, bbdd):
        self.bbdd = bbdd


    def conectarBBDD(self):
        
        self.miConex = sqlite3.connect(self.bbdd)
        self.miCursor = self.miConex.cursor()
            
        try:
            
            self.miCursor.execute("""--sql
                    CREATE TABLE DATOSUSUARIOS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE VARCHAR(20), APELLIDO VARCHAR(20),
                    CONTRASEÑA VARCHAR(20), DIRECCION VARCHAR(20),
                    COMENTARIOS VARCHAR(100))
            """)
            
            msg.showinfo("BB. DD.", "¡La base de datos ya está lista!")

        except:
            msg.showwarning("Atención", "La base de datos ya está creada.")


    def closeBBDD(self):
        self.miConex.close()


usuarios = Conexion("usuarios.db")

def salirAplicacion():
    valor = msg.askokcancel("Salir", "¿De verdad quieres salir?")
    if valor == True:
        try:
            usuarios.closeBBDD()
        finally:
            root.destroy()

#_____________RESET CAMPOS_____________________

def borrarCampos():
    global inputSQL
    
    cuadroID.delete(0, END)
    cuadroNombre.delete(0, END)
    cuadroApellido.delete(0, END)
    cuadroPass.delete(0, END)
    cuadroDireccion.delete(0, END)
    textoComentario.delete('1.0', END)
       
    
#_____________CRUD_MENU_____________________

def inputCRUD(nom_c, ape_c, contr_c, dire_c, coment_c):
    inputSQL = [(nom_c, ape_c, contr_c, dire_c, coment_c)]

def insertInto():
    global inputSQL
    global usuarios
    
    cuadroID.delete(0, END)
    
    inputSQL = [(cuadroNombre.get(), cuadroApellido.get(), cuadroPass.get(
    ), cuadroDireccion.get(), textoComentario.get('1.0', END))]
    
    usuarios.miCursor.execute(
        "INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)", inputSQL)
    usuarios.miConex.commit()
    
    msg.showinfo("BB. DD.", "Registro insertado con éxito.")


def selectFrom():
    global inputSQL
    global usuarios
    
    try:
        inputSQL = [(cuadroID.get())]
        
        borrarCampos()
        
        usuarios.miCursor.execute(
            "SELECT * FROM DATOSUSUARIOS WHERE ID=(?)", inputSQL)
        
        busqueda = usuarios.miCursor.fetchall()
        selectID.set(busqueda[0][0])
        selectNom.set(busqueda[0][1])
        selectApe.set(busqueda[0][2])
        selectPass.set(busqueda[0][3])
        selectDir.set(busqueda[0][4])
        textoComentario.insert('1.0', busqueda[0][5])
        
        usuarios.miConex.commit()
    
    except IndexError:
        msg.showwarning("Atención", "No existe ningún registro con esa ID.")


def updateSet():
    global inputSQL
    global usuarios

    try:
        inputSQL = [(cuadroNombre.get(), cuadroApellido.get(), cuadroPass.get(
        ), cuadroDireccion.get(), textoComentario.get('1.0', END), cuadroID.get())]

        usuarios.miCursor.execute(
            "UPDATE DATOSUSUARIOS SET NOMBRE=(?), APELLIDO=(?), CONTRASEÑA=(?), DIRECCION=(?), COMENTARIOS=(?) WHERE ID=(?)", inputSQL
                                    )
        
        usuarios.miConex.commit()
        
        msg.showinfo("BB. DD.", "Registro actualizado con éxito.")
    
    except IndexError:
        msg.showwarning("Atención", "No existe ningún registro con esa ID.")


def deleteFrom():
    global inputSQL
    global usuarios
    
    inputSQL = [(cuadroID.get())]

    usuarios.miCursor.execute(
        "SELECT * FROM DATOSUSUARIOS WHERE ID=(?)", inputSQL)

    comprobacion = usuarios.miCursor.fetchall()

    try:
        selectID.set(comprobacion[0][0])
    
        usuarios.miConex.commit()
            
        usuarios.miCursor.execute(
            "DELETE FROM DATOSUSUARIOS WHERE ID=(?)", inputSQL)
        usuarios.miConex.commit()
            
        msg.showinfo("BB. DD.", "Registro eliminado con éxito.")
    
    except IndexError:
        msg.showwarning("Atención", "No existe ningún registro con esa ID.")



#______________INFO____________________

def avisoLicencia():
    msg.showinfo("Licencia", "Producto bajo licencia GNU")

# Ahí va el cuadro de Acerca de...
def infoAdicional():
    msg.showinfo("---VICIOS EDITORIALES",
                        "CRUD para BB. DD. \nv.1.220316.1")


#____________Botones_MENU______________

barraMenu = Menu(root)
root.config(menu=barraMenu)

menuBBDD = Menu(barraMenu)
menuBBDD.add_command(label="Conectar", underline=2,
                     command=usuarios.conectarBBDD)
menuBBDD.add_command(label="Salir", underline=0, command=salirAplicacion)

menuCRUD = Menu(barraMenu)
menuCRUD.add_command(label="Crear", underline=0, command=insertInto)
menuCRUD.add_command(label="Leer", underline=0, command=selectFrom)
menuCRUD.add_command(label="Actualizar", underline=2, command=updateSet)
menuCRUD.add_command(label="Eliminar", underline=0, command=deleteFrom)

menuAyuda = Menu(barraMenu)
menuAyuda.add_command(label="Licencia", underline=1, command=avisoLicencia)
menuAyuda.add_command(label="Acerca de…", underline=0, command=infoAdicional)

barraMenu.add_cascade(label="BB. DD.", menu=menuBBDD)
barraMenu.add_command(label="Borrar", underline=0, command=borrarCampos)
barraMenu.add_cascade(label="CRUD", menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)


#----------------------CAMPOS ENTRY------------------------

cuadroID = Entry(miFrame, textvariable=selectID,
                 width=16, font=("Bookerly", 12))
cuadroID.grid(row=0, column=1, sticky="w", padx=10, pady=10)
cuadroID.config(fg="steelblue", bg="lavender")

cuadroNombre = Entry(miFrame, textvariable=selectNom, width=16, font=("Bookerly", 12))
cuadroNombre.grid(row=1, column=1, sticky="w", padx=10, pady=10)

cuadroApellido = Entry(miFrame, textvariable=selectApe, width=16, font=("Bookerly", 12))
cuadroApellido.grid(row=2, column=1, sticky="w", padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=selectPass, width=16, font=("Bookerly", 12))
cuadroPass.grid(row=3, column=1, sticky="w", padx=10, pady=10)
cuadroPass.config(show="*")  # con esto solo se ven asteriscos, no las letras

cuadroDireccion = Entry(miFrame, textvariable=selectDir, width=16, font=("Bookerly", 12))
cuadroDireccion.grid(row=4, column=1, sticky="w", padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5, font=("Bookerly", 12))
textoComentario.grid(row=5, column=1, padx=10, pady=10)
# Creamos la barra vertical y configuramos para que sea vertical en textoComentario
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
# Ahora tenemos que colocarla para que funcione:
scrollVert.grid(row=5, column=2, sticky="nsew")
# Para que la barra se posicione bien de acuerdo con la longitud.
textoComentario.config(yscrollcommand=scrollVert.set)


#_________CAMPOS_RÓTULOS____________________

idLabel = Label(miFrame, text="ID:", font=("Consolas", 12), bg="moccasin", fg='steelblue')
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:", font=("Consolas", 12), bg="moccasin")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:", font=("Consolas", 12), bg="moccasin")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:", font=("Consolas", 12), bg="moccasin")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:", font=("Consolas", 12), bg="moccasin")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:", font=("Consolas", 12), bg="moccasin")
comentariosLabel.grid(row=5, column=0, sticky="ne", padx=10, pady=10)


#___________BOTONES_CRUD____________________

botonCreate = Button(miFrameCRUD, text="Create", font=("Consolas", 10), command=insertInto)
botonCreate.grid(row=0, column=0, padx=10, pady=10)

botonRead = Button(miFrameCRUD, text="Read", font=("Consolas", 10), command=selectFrom)
botonRead.grid(row=0, column=1, padx=10, pady=10)

botonUpdate = Button(miFrameCRUD, text="Update", font=("Consolas", 10), command=updateSet)
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonDelete = Button(miFrameCRUD, text="Delete", font=("Consolas", 10), command=deleteFrom)
botonDelete.grid(row=0, column=3, padx=10, pady=10)





#------------FIN----------------------
root.mainloop()

