from django.http import HttpResponse
from django.template import Template, Context
#Cargador plantillas => OJO: hay que añadir templates dir en settings.py
from django.template import loader
from django.shortcuts import render

def hello_world(request):
    doc_externo = open("test_django/templates/hello_world.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def hello_name(requtest):
    name = "Anxo Gesto"
    doc_externo = open("test_django/templates/hello_name.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({
        "nombre": name
    })
    documento = plt.render(ctx)
    return HttpResponse(documento)

def bucles(request):
    doc_externo = open("test_django/templates/bucles.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({
        "nombre": "Anxo",
        "temas": ["tema1", "tema2", "tema3"]
    })
    documento = plt.render(ctx)
    return HttpResponse(documento)

def cargadores_1(request):
    tmpt = loader.get_template("hello_name.html")
    documento = tmpt.render({"nombre":"Anxo"})
    return HttpResponse(documento)

def cargadores_2(request):
    return render(request, "hello_name.html", {"nombre": "Pepe"})

def plantilla_incrustada(request):
    return render(request, "plantilla_incrustada.html", {"nombre": "Pepe"})