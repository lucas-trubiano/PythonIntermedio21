#pip install firebase-admin #libreria oficial de firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import matplotlib.pyplot as plt
import plotly.express as px
import time

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Volumes/HDD 500/PROYECTOS/IoT/Firebase/iothuerta-firebase-adminsdk-bhgyv-123b081146.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iothuerta-default-rtdb.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('Datos/esp0001/2021')
for i in range(10):
    print(time.time())
    dato = {
                "time":round(time.time()),#21,31,41...
                "temperature":25+i,
                "humidity":80-i     }
    ref.push(dato)

#ref = db.reference('Datos/esp0001/2021')
datos = ref.get()
tm = []
temp = []
humid = []

for key in datos:
    print(datos[key])
    tm.append(datos[key]["time"])
    temp.append(datos[key]["temperature"])
    humid.append(datos[key]["humidity"])


fig = px.scatter(x=tm,y=temp)
fig.update_traces(mode='lines+markers')
fig.write_html('history.html',
               include_plotlyjs='cdn',
               full_html=False,
               include_mathjax='cdn')
fig.show()
# print(ref.set(dato))
# ref.push({"temperature":12,
# "humedad":34})