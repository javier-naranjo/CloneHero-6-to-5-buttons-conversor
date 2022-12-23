import os
import shutil
import configparser
import csv
import re
from tkinter import *
from tkinter import filedialog

#///////////////////////////////////////////////////////////////////////////////////////
def Explorar():
    global Elejida
    global b_explorar
    global directorio
    directorio = filedialog.askdirectory()
    if directorio:
        b_explorar['text'] = "Espere..."
        b_explorar['state'] = DISABLED
        mensaje.set("ESPERA UN MOMENTO, esto puede tardar varios minutos.\nNo cierres la ventana")
        Elejida.set("Se ha configurado: \n" + directorio)
        config = configparser.ConfigParser()
        for carpeta, subcarpetas, archivos in os.walk(directorio):
            if carpeta != directorio:
                for x in archivos:
                    if x.endswith("notes.mid"):
                        try:
                            shutil.copy(os.path.join(carpeta, x), os.path.join(carpeta, "notes.bak"))
                            cambiarMidi(carpeta, x)
                        except Exception as e:
                            print(e)
                    if x.endswith("song.ini"):
                        try:
                            config.read(os.path.join(carpeta, x))
                            shutil.copy(os.path.join(carpeta, x), os.path.join(carpeta, "song.bak"))
                            if config.has_section('Song') and config.has_section('song') == False:
                                CambiarNombre(config, 'Song', 'song')
                            if config.has_section('Song'):
                                config.remove_section('Song')
                            valor = config.get('song', 'diff_guitarghl')
                            config.set('song', 'diff_guitar', valor)
                            with open(os.path.join(carpeta, x), 'w') as conf:
                                config.write(conf)
                            conf.close()
                            config.clear()
                        except Exception as e:
                            print(e)
                            config.clear()
        b_explorar['text'] = "LISTO!"                
        mensaje.set("DONE! Ya puedes cerrar la ventana")
        os.remove(os.path.join(os.getcwd(), "convertir.cmd"))
        os.remove(os.path.join(os.getcwd(), "input.csv"))
        os.remove(os.path.join(os.getcwd(), "output1.csv"))
        os.remove(os.path.join(os.getcwd(), "output2.csv"))
        os.remove(os.path.join(os.getcwd(), "output3.csv"))
        os.remove(os.path.join(os.getcwd(), "parchar.cmd"))

#///////////////////////////////////////////////////////////////////////////////////////
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ',' + ele
    return str1[1:]

#///////////////////////////////////////////////////////////////////////////////////////
def CambiarNombre(x, origen, final):
    items = x.items(origen)
    x.add_section(final)
    for item in items:
        x.set(final, item[0], item[1])
    x.remove_section(origen)

#///////////////////////////////////////////////////////////////////////////////////////
def cambiarMidi(pat, mi):
    global directorio
    f = open("convertir.cmd","w+")
    f.write('"' + os.getcwd() + '\midicsv-1.1\Midicsv.exe"' + ' "' + os.path.join(pat, mi) + '" ' + "> " + '"' + os.getcwd() + '\input.csv"')
    f.close()
    os.system("convertir.cmd")
    
    text = open("input.csv", "r")
    text = ''.join([i for i in text]).replace("PART GUITAR GHL", "PART GUITAR") \
        .replace(", 0, 100, 100",", 0, 110, 100").replace(", 0, 100, 0",", 0, 110, 0") \
        .replace(", 0, 99, 100",", 0, 109, 100").replace(", 0, 99, 0",", 0, 109, 0") \
        .replace(", 0, 98, 100",", 0, 108, 100").replace(", 0, 98, 0",", 0, 108, 0") \
        .replace(", 0, 97, 100",", 0, 112, 100").replace(", 0, 97, 0",", 0, 112, 0") \
        .replace(", 0, 96, 100",", 0, 111, 100").replace(", 0, 96, 0",", 0, 111, 0") \
        .replace(", 0, 112, 100",", 0, 100, 100").replace(", 0, 112, 0",", 0, 100, 0") \
        .replace(", 0, 111, 100",", 0, 99, 100").replace(", 0, 111, 0",", 0, 99, 0") \
        .replace(", 0, 110, 100",", 0, 98, 100").replace(", 0, 110, 0",", 0, 98, 0") \
        .replace(", 0, 109, 100",", 0, 97, 100").replace(", 0, 109, 0",", 0, 97, 0") \
        .replace(", 0, 108, 100",", 0, 96, 100").replace(", 0, 108, 0",", 0, 96, 0") \
        .replace(", 0, 95, 100",", 0, 97, 100").replace(", 0, 95, 0",", 0, 97, 0")
    x = open("output1.csv","w")
    x.writelines(text)
    x.close()

    count = 0
    l_orig = []
    l_camb = []
    csv_file = csv.reader(open('input.csv', "r"), delimiter=",")
    for row in csv_file:
        count += 1
        try:
            if row[4] == " 94" and row[2] == " Note_on_c":
                inilist = [i.start() for i in re.finditer(",", listToString(row))]
                l_orig.append(listToString(row))
                l_camb.append(listToString(row)[:inilist[1]+1] + " System_exclusive, 8, 80, 83, 0, 0, 3, 1, 1, 247")
            if row[4] == " 94" and row[2] == " Note_off_c":
                inilist = [i.start() for i in re.finditer(",", listToString(row))]
                l_orig.append(listToString(row))
                l_camb.append(listToString(row)[:inilist[1]+1] + " System_exclusive, 8, 80, 83, 0, 0, 3, 1, 0, 247")
        except:
            pass
    
    cuenta = 0
    text = open("output1.csv", "r")
    text = ''.join([i for i in text])
    for raw in l_orig:
        text = text.replace(raw, raw + "\n" + l_camb[cuenta])
        cuenta +=1 
    x = open("output3.csv","w")
    x.writelines(text)
    x.close()

    text = open("output3.csv", "r")
    text = ''.join([i for i in text]).replace(", 0, 94, 100",", 0, 96, 100").replace(", 0, 94, 0",", 0, 96, 0")
    x = open("output2.csv","w")
    x.writelines(text)
    x.close()

    f = open("parchar.cmd","w+")
    f.write('"' + os.getcwd() + '\midicsv-1.1\Csvmidi.exe"' + ' "' + os.getcwd() + '\output2.csv"' + " > " + '"' + os.path.join(pat, mi) + '"')
    f.close()
    os.system("parchar.cmd")

#///////////////////////////////////////////////////////////////////////////////////////
directorio = ""
root = Tk()
Elejida = StringVar()
mensaje = StringVar()
mensaje.set("Este programa te permite cambiar los charts .mid de canciones 6 botones \nDe manera que pasen a ser para guitarra convencional 5 colores en Clone Hero")
lbl1 = Label(master=root,textvariable=Elejida)
lbl1.grid(row=2, column=0)
lbl2 = Label(master=root,textvariable=mensaje)
lbl2.grid(row=0, column=0)
b_explorar = Button(text="Buscar Capeta", command=Explorar)
b_explorar.grid(row=1, column=0)
Lower_left = Label(root,text ='Silly Python Script by J.Naranjo 2022')
Lower_left.place(relx = 0.0, rely = 1.0, anchor ='sw')
root.geometry("450x300")
root.title('RetroAntena - Charts de 6 a 5 botones (Clone Hero)')
mainloop()