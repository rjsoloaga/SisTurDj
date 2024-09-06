from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista de bienvenida
def bienvenida(request):
    return HttpResponse("<h1 style='color: red;'>Bienvenido a Body Center</h1>")

def horaActual(request):
    respuesta = "<h2>La Hora es: {0}</h2>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def index(request):
    empresa = "Center Body"
    servicios = ["Depilacion", "Cejas y Pestañas","Tratamiento Corporal", "Tratamiento Facial", "Masajes", "Podoestetica", "Manicura"]
    # Abrimos el documento que contiene la plantilla:
    plantillaExterna = open("C:\\Users\\javie\\OneDrive\\Escritorio\\SisTurDj\\Proyecto\\Proyecto\\templates\\index.html")
    # Cargamos el documento en una variable de tipo 'Template':
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    # Crear un contexto:
    contexto = Context({"empresa": empresa , "servicios": servicios})
    # Renderizar el documento:
    documento = template.render(contexto)
    
    return HttpResponse(documento)

def plantillaParametro(request):
    BodyCenter = "Body Center"
    # Abrimos el documento que contiene la plantilla:
    plantillaExterna = open("C:\\Users\\javie\\OneDrive\\Escritorio\\SisTurDj\\Proyecto\\Proyecto\\templates\\nombreEmpresa.html")
    # Cargamos el documento en una variable de tipo 'Template':
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    # Crear un contexto:
    contexto = Context({"nombreEmpresa": BodyCenter})
    # Renderizar el documento:
    documento = template.render(contexto)
    
    return HttpResponse(documento)