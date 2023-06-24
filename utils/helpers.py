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
    config = {
        'distancia': [3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79,83,87,91,95]  
    }
    
    registro['data']['distancia'] = config
    for registro in registros["data"]:
        if registro.get("fecha") == fecha:
            html = template.render(registro)
            pdfkit.from_string(html,f'consulta_{fecha}.pdf',options=options)
    # ,configuration=pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


