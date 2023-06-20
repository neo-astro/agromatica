from fastapi import FastAPI
from fastapi.responses import FileResponse
import time
#para visualizar los datos del cursor que devuelve el method find oeoeoeoeoeoeoeooeoeoe
from bson import ObjectId
#db
from config.db import client

from models.data import Data,DataRealTime

from schemas.dataSchemas import datosEntity
import random
from utils.helpers import crearPdf
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

@app.get("/consultas/{fecha}")
async def generar_pdf(fecha:str):
    if fecha:
        var = {
    "data": [
        {
            "_id": "648e5b3d46448fa5c63d3828",
            "fecha": "2023-10-10",
            "senHumedadAire": [58],
            "senHumedadAgua": [85],
            "senPh": [85],
            "senCalidadAire": [9]
        },
        {
            "_id": "648f39edf219464fa596fb27",
            "id": "string",
            "fecha": "string",
            "senHumedadAgua": "string",
            "senHumedadAire": "string",
            "senPh": "string",
            "senCalidadAire": "string"
        },
        {
            "_id": "648f39fba47ae2620cb5f2c5",
            "id": "string",
            "fecha": "string",
            "senHumedadAgua": "string",
            "senHumedadAire": "string",
            "senPh": "string",
            "senCalidadAire": "string"
        },
        {
            "_id": "648f3e49722fca362a37045b",
            "fecha": "2023-06-18",
            "senHumedadAgua": [
                "string"
            ],
            "senHumedadAire": [
                "string"
            ],
            "senPh": [
                "string"
            ],
            "senCalidadAire": [
                "string"
            ]
        }
    ]
}
        nombreArchivo = f'consulta_{fecha}.pdf'
        crearPdf(fecha,var)
        ruta_archivo = nombreArchivo  # Ruta al archivo PDF en tu servidor
        time.sleep(2)
        return FileResponse(path=nombreArchivo,filename= nombreArchivo)

 