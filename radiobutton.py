from tkinter import *


window = Tk()

window.columnconfigure(0, weight =1)
window.columnconfigure(1, weight=2)

lrBpregunta = Label(window, text= 'te sientes listo').place(x=100, y=100)

seleccionado = IntVar(value=0) # Agregar una opción "ninguno" con valor 0
rdBopcion1 = Radiobutton(window, text= '', value='0', variable = seleccionado).place(x=100,y=130)
rdBopcion1 = Radiobutton(window, text= 'si', value='1', variable = seleccionado).place(x=100,y=130)
rdBopcion1 = Radiobutton(window, text= 'no', value='2', variable = seleccionado).place(x=100,y=150)
rdBopcion1 = Radiobutton(window, text= 'nose', value='3', variable = seleccionado).place(x=100,y=170)
rdBopcion1 = Radiobutton(window, text= 'tal vez', value='4', variable = seleccionado).place(x=100,y=190)

btnDeseleccionar = Button(window, text='Deseleccionar', command=lambda: seleccionado.set(0))
btnDeseleccionar.place(x=100, y=240)

window.mainloop()