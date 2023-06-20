from fastapi import FastAPI
#para visualizar los datos del cursor que devuelve el method find oeoeoeoeoeoeoeooeoeoe
from bson import ObjectId
#db
from config.db import client

from models.data import Data,DataRealTime

from schemas.dataSchemas import datosEntity
import random

app = FastAPI()

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
def getRealTimeData():
    for i in senMedicion:
        senMedicion[i] = random.randint(0,101)
    return senMedicion

#obtener los datos en tiempo real
@app.post("/realTimeData")
def getRealTimeData(data : DataRealTime):
    senMedicion['senHumedadAgua'].append(data.senHumedadAgua)
    senMedicion['senHumedadAire'].append(data.senHumedadAire)  
    senMedicion['senPh'].append(data.senPh)
    senMedicion['senCalidadAire'].append(data.senPh) 

@app.get("/home")
def getAllData():
    cursor = DbRegistros.find()
    data = [doc for doc in cursor]

    for doc in data:
        doc['_id'] = str(doc['_id'])
    return {'data': data}

@app.post("/addData")
def addData(data:Data):

    newData= dict(data)
    id = DbRegistros.insert_one(newData).inserted_id   
    print(newData)
    return str(id)
