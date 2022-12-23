import os

for carpeta, subcarpetas, archivos in os.walk(os.getcwd()):
    if carpeta != os.getcwd():
        for x in archivos:
            if x.endswith("notes.mid"):
                print("Configurando: ", os.path.join(carpeta, x))
                os.remove(os.path.join(carpeta, x))
            if x.endswith("song.ini"):
                os.remove(os.path.join(carpeta, x))

for carpeta, subcarpetas, archivos in os.walk(os.getcwd()):
    if carpeta != os.getcwd():
        for x in archivos:
                if x.endswith("notes.bak"):
                    os.rename(os.path.join(carpeta, x), os.path.join(carpeta, "notes.mid"))
                if x.endswith("song.bak"):
                    os.rename(os.path.join(carpeta, x), os.path.join(carpeta, "song.ini"))