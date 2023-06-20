import datetime
import time
import os

from jinja2 import Environment, FileSystemLoader
import pdfkit
import tempfile



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
    
    # for registro in registros["data"]:
    #     if registro.get("fecha") == fecha:
    #         html = template.render(registro)
    #         pdfkit.from_string(html,f'consulta_{fecha}.pdf',options=options)


    #generar pdf en ejecucion
    for registro in registros["data"]:
        if registro.get("fecha") == fecha:
            html = template.render(registro)

            # Crear un archivo temporal para almacenar el HTML
            with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as temp_file:
                temp_file.write(html.encode("utf-8"))
                temp_file.close()

                # Convertir el HTML a PDF utilizando pdfkit y wkhtmltopdf
                pdf_bytes = pdfkit.from_file(temp_file.name, False, options=options)

            # Eliminar el archivo temporal
            temp_file.unlink()

            return pdf_bytes
