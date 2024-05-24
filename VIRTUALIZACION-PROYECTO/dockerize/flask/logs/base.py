from firebase import firebase
import pyrebase

Connection = firebase.FirebaseApplication('#link', None)
firebaseConfig ={#credenciales}

while True:
    #inicializa pyrebase
    counter=0
    firebase = pyrebase.initialize_app(firebaseConfig)
    db=firebase.database()
    #verificacion
    if not db.child('Logs').shallow().get().val():
        #no hay nada aun en la base de datos
        #1. Leer el archivo
        f = open("access.log", "r")
        lines = f.readlines()
        #escribir archivo
        count = 0
        for line in lines:
            count += 1
            linea = line.strip()
            data = {
                'LOG' : linea
            }
            result = Connection.post('/Logs/', data)
        print(count)
    else:
        #Existen logs
        #Consultar cantidad
        counter = 0
        result= db.child("Logs").get()
        for res in result.each():
            counter += 1
        print("total", counter)
        #escribir nuevos en el archivo
        f = open("access.log", "r")
        lines = f.readlines()
        count1 = 0
        for line in lines:
            count1 += 1
            linea = line.strip()
            if count1 == (counter+1) or count1 > (counter+1):
                data = {
                    'LOG' : linea
                }
                result = Connection.post('/Logs/', data)
