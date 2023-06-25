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

def crearPdf(fecha,registros):
    valor_dis = 3
    config = {}
    new_registro = []
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

    for i in registros:
        new_registro.append(i)

    for obj in new_registro:
        for clave in obj:
            if clave == 'senHumedadAgua' or clave ==  'senPh' or clave ==  'senHumedadAire' or clave ==  'senCalidadAire' :
                obj[clave] = [new_registro[clave], valor_dis] 
                valor_dis += 4


    for registro in registros:
        if registro.get("fecha") == fecha:
            registro['distancia']= config
            html = template.render(new_registro)
            pdfkit.from_string(html,f'consulta_{fecha}.pdf',options=options)

    # ,configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


