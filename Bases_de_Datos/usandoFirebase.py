import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Volumes/HDD 500/PROYECTOS/repos git/PythonIntermedio21/Bases_de_Datos/iothuerta-firebase-adminsdk-bhgyv-123b081146.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iothuerta-default-rtdb.firebaseio.com'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('Datos')
dato = {"temperature":35}
print(ref.set(dato))
ref.push({"temperature":12,
"humedad":34})