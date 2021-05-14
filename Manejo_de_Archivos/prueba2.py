# 1)
a="/IA2/TP1/orders.txt"
b="/TP1/orders.txt"
c="TP1/orders.txt"             #this
d="IA2/TP1/orders.txt"
e="orders.txt"
X = c
f = open(X)
f.close()

# 2)
import os

path, _ = os.path.split(os.path.abspath(__file__))
f = open(path+"/saludo.txt")
# El archivo contiene
"""
Bienvenidos al manejo de archivos con python
Mi nombre es Lucas
Trabajo en Casa del futuro godoy cruz
Adios
"""


