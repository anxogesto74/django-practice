from django.shortcuts import render

# Create your views here.
"""GESTION BASE DE DATOS
    ·Almacenar nueva entrada
        ej = modelo(atributo=valor, atributo=valor)
        ej.save() => se guarda
        ej2 = Modelo.objects.create(atributo=valor, atributo=valor)
    ·Actualizar:
        ej.atributo = nuevo_valor
        ej.save()
    ·Select:
        ej3 = Modelo.objects.get(articulo=valor)
        lista = Modelo.objects.all() -> select *
            -> podemos hacer lista.query.__str__() y tenemos la instruccion select que se ejecuta por debajo
    ·Delete:
        ej3.delete()

COMPARACIONES => 
    precio>100 ---- precio__gte = 100
    precio<100 ---- precio__gte = 100
    ejemplo: Articulos.objects.filter(precio__gte=50, precio__lte=150) precio>50 y <150
             precio__range(50,150)

ORDENAR RESULTADOS =>
    Articulos.objects.filter(condiciones).order_by(atributo)
    Articulos.objects.filter(condiciones).order_by('-atributo') -> desc poniendo un - delante del nombre del atributo
"""
