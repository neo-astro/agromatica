from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#para visualizar los datos del cursor que devuelve el method find
from bson import ObjectId
#db
from config.db import client

from models.data import Data,DataRealTime

from schemas.dataSchemas import datosEntity
import random

from utils.helpers import *


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
    # Agrega aquí los dominios permitidos para acceder a tu API
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DbRegistros=client.DbAgromatica.Registros


#datos para mostrar en tiempo real
senMedicion = {
        "senHumedadAgua": 0,
        "senHumedadAire": 0,
        "senPh":          0,
        "senCalidadAire": 0
}

#en la base de datos se guardara el promedio de la medicion de los sensores por horas


#entregar datos al frontend en tiempo real
@app.get("/")
def getRealTime():
    for i in senMedicion:
        senMedicion[i] = random.randint(0,101)
    return senMedicion



#para ver los registros de la db
@app.get("/verDatos")
def getAllData():
    cursor = DbRegistros.find()
    data = [doc for doc in cursor]

    for doc in data:
        doc['_id'] = str(doc['_id'])
    return {'data': data}







#guardar datos para tiempo real

@app.post("/saveData")
def saveData(datos):
    hora = str(getHora())
    # el tipo de diccionario que me envia
    registro = {
        "fecha":    getHora(),
        "senHumedadAgua": {},
        "senHumedadAire": {},
        "senPh":          {},
        "senCalidadAire": {}
    }

    query = {'fecha':datos.get('fecha')}
    consultaRegistro = DbRegistros.find_one(query)

    if consultaRegistro:
        consultaRegistro['senHumedadAgua'][hora] = datos.get('senHumedadAgua')
        consultaRegistro['senHumedadAire'][hora] = datos.get('senHumedadAire')
        consultaRegistro['senPh'][hora] = datos.get('senPh')
        consultaRegistro['senCalidadAire'][hora] = datos.get('senCalidadAire')

        #actualizar dato
        consultaRegistro.update_one({'_id': consultaRegistro['_id']}, {'$set': consultaRegistro})
        return 'ok'
    else :
        registro['senHumedadAgua'][hora] = datos.get('senHumedadAgua')
        registro['senHumedadAire'][hora] = datos.get('senHumedadAire')
        registro['senPh'][hora] = datos.get('senPh')
        registro['senCalidadAire'][hora] = datos.get('senCalidadAire')
        newRegistro  = dict(registro) 
        DbRegistros.insert_one(newRegistro) 
        return 'error'






    # newData= dict(datos)
    # id = DbRegistros.insert_one(newData).inserted_id   
    # print(newData)
    # return str(id)
@app.post("/prueba")
def prueba():
    return 'dato'


#obtener los datos en tiempo real
@app.post("/realTimeData")
def getRealTimeData(data : DataRealTime):
    senMedicion['senHumedadAgua'].append(data.senHumedadAgua)
    senMedicion['senHumedadAire'].append(data.senHumedadAire)  
    senMedicion['senPh'].append(data.senPh)
    senMedicion['senCalidadAire'].append(data.senPh) 






# @app.post("/addData")
# def addData(dato:Data):
#     newData= dict(dato)
#     id = DbRegistros.insert_one(newData).inserted_id   
#     print(newData)
#     return str(id)



