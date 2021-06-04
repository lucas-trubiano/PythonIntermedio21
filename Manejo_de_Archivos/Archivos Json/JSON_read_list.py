import json # https://www.analyticslane.com/2018/07/16/archivos-json-con-python/
import os

path, _ = os.path.split(os.path.abspath(__file__))

with open(path+f'/WriteClientes.json') as file:
    clientes = json.load(file)

print(type(clientes))
for elemento in clientes:
    print(elemento)