import datetime
import time
import os

from jinja2 import Environment, FileSystemLoader
import pdfkit



def getHora():
    return time.strftime('%H')


def getDate():
    fecha_actual = datetime.date.today()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")
    return fecha_formateada


var = {
    "data": [
        {
            "_id": "648e5b3d46448fa5c63d3828",
            "fecha": "2023/10/10",
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

def crearPdf(fecha,registros):
    # Cargar el template
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")

    options = {
        'page-size': 'A5',
        'margin-top': '0.1in',
        'margin-right': '0.1in',
        'margin-bottom': '0.1in',
        'margin-left': '0.1in'
    }
    
    for registro in registros["data"]:
        if registro.get("fecha")== fecha:
            html = template.render(registro)
            pdfkit.from_string(html,f'consulta_{fecha}.pdf',options=options, configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'))
            ##print(registro)
# crearPdf('2023/10/10',var)
