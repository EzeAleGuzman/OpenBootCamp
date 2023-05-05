from tkinter import *

window = Tk()
window.geometry("800x600+0+0")
window.title("listabox")
lblNombres = Label(window, text='nombres: ').place(x=100,y=100)
nombres = Listbox(window )

for item in ['juan', 'laura', 'angel', 'ezequiel', 'oscar', 'Maria', 'estefania', 'dominic']:
 nombres.insert(END, item)
nombres.place(x=100, y =120)
window.mainloop()