from fastapi import FastAPI
#para visualizar los datos del cursor que devuelve el method find
from bson import ObjectId
#db
from config.db import client

from models.data import Data,DataRealTime




from schemas.dataSchemas import datosEntity


app = FastAPI()

DbRegistros=client.DbAgromatica.Registros


#datos para mostrar en tiempo real
SenMedicion = {
        "senHumedadAgua": [],
        "senHumedadAire": [],
        "senPh":          [],
        "senCalidadAire": []
}
#en la base de datos se guardara el promedio de la medicion de los sensores por horas

@app.get("/")
def getRealTimeData():
    return SenMedicion

@app.post("/realTimeData")
def getRealTimeData(data : DataRealTime):
    SenMedicion['senHumedadAgua'].append(data.senHumedadAgua)
    SenMedicion['senHumedadAire'].append(data.senHumedadAire)  
    SenMedicion['senPh'].append(data.senPh)
    SenMedicion['senCalidadAire'].append(data.senPh) 



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
