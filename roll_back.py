import os
from tkinter import *
from tkinter import filedialog

#///////////////////////////////////////////////////////////////////////////////////////
def CambiarNombre(x, origen, final):
    items = x.items(origen)
    x.add_section(final)
    for item in items:
        x.set(final, item[0], item[1])
    x.remove_section(origen)

#///////////////////////////////////////////////////////////////////////////////////////
def Explorar():
    global Elejida
    directorio = filedialog.askdirectory()
    if directorio:
        Elejida.set("Se ha configurado: \n" + directorio)
        for carpeta, subcarpetas, archivos in os.walk(directorio):
            if carpeta != directorio:
                for x in archivos:
                    if x.endswith("notes.mid"):
                        print("Configurando: ", os.path.join(carpeta, x))
                        os.remove(os.path.join(carpeta, x))
                    if x.endswith("song.ini"):
                        os.remove(os.path.join(carpeta, x))
        for carpeta, subcarpetas, archivos in os.walk(directorio):
            if carpeta != directorio:
                for x in archivos:
                    if x.endswith("notes.bak"):
                        os.rename(os.path.join(carpeta, x), os.path.join(carpeta, "notes.mid"))
                    if x.endswith("song.bak"):
                        os.rename(os.path.join(carpeta, x), os.path.join(carpeta, "song.ini"))
        mensaje.set("DONE! Ya puedes cerrar la ventana")

#///////////////////////////////////////////////////////////////////////////////////////
root = Tk()
Elejida = StringVar()
mensaje = StringVar()
mensaje.set("Este programa te permite regresar todos los archivos modificados \na su estado original...")
lbl1 = Label(master=root,textvariable=Elejida)
lbl1.grid(row=2, column=0)
lbl2 = Label(master=root,textvariable=mensaje)
lbl2.grid(row=0, column=0)
b_explorar = Button(text="Buscar Capeta", command=Explorar)
b_explorar.grid(row=1, column=0)
Lower_left = Label(root,text ='Silly Python Script by J.Naranjo 2022')
Lower_left.place(relx = 0.0, rely = 1.0, anchor ='sw')
root.geometry("450x300")
root.title('UNDO Video Start Time (Clone Hero)')
mainloop()