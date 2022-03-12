from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import  get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #primera vista

    p1 = Persona(" Alumno Jaime", "Trujillo")

    #nombre="Jaime"
    #apellido = "Trujillo"
    temas_curso=["Plantillas", "Modelos","Formularios", "Vistas", "Despliegue"]
    #fecha_actual = datetime.datetime.now()
    #doc_externo = open("C:/Users/atang/PycharmProjects/TESTDB/TESTDB/TESTDB/Templates/template.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = get_template('template.html')

    #ctx=Context({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha_actual": fecha_actual, "temas":temas_curso})
    #documento = doc_externo.render({"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "fecha_actual": fecha_actual, "temas":temas_curso})
    return render(request, "template.html", {"nombre_persona": p1.nombre, "apellido_persona": p1.apellido, "temas":temas_curso})

def despedida(request): #primera vista
    return HttpResponse("Adios Mundo  DJANGO")

def dameFecha(request): #primera vista
    fecha_actual=datetime.datetime.now()
    documento = "<html><body></body><h1>Fecha y hora actuales %s</h1></html>"%fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad, agno):
    #edadActual = 18
    periodo= agno - 2022
    edadFutura = edad + periodo
    documento = "<html><body><h1>En el año %s tendrás %s años</h1></body></html>" % (agno, edadFutura)

    return HttpResponse(documento)

def cursoC(request):

 fecha_actual = datetime.datetime.now()

 return render(request, "CursoC.html", {"dameFecha": fecha_actual})


def cursoCss(request):

 fecha_actual = datetime.datetime.now()

 return render(request, "CursoCss.html", {"dameFecha": fecha_actual})
