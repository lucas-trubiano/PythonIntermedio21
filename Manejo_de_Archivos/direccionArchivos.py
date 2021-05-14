import os
#https://www.delftstack.com/es/howto/python/how-to-get-the-current-script-file-directory/
#https://recursospython.com/guias-y-manuales/os-shutil-archivos-carpetas/
#print("Ruta:","/Volumes/HDD 500/Tutoriales/Curso Python Intermedio/ManejoArchivos/texto.txt")
#print("Directorio de trabajo:",os.getcwd())

absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
#print(f"Script file path is {path}, filename is {filename}")
#print(path+"/saludo.txt")
f = open(path+"/saludo.txt")

for linea in f:
    print(linea,end="")
print()
f.close()
