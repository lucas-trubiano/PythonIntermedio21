import json # https://www.analyticslane.com/2018/07/16/archivos-json-con-python/
import os

path, _ = os.path.split(os.path.abspath(__file__))

data = {} # creo un diccionario

data["empresa"] = "Python"

data['clients'] = [] # creo la categoria clientes,
# como una lista de "Objetos" del tipo diccionarios.

data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})

with open(path+'/WriteData.json', 'w') as file:
    json.dump(data, file, indent=4)
