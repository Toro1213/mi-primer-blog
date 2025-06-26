# rugby/views.py
from django.shortcuts import render
from .models import JugadorRugby

def lista_rugby(request):
    jugadores = JugadorRugby.objects.all()

    # Obtener filtros desde el formulario
    nombre = request.GET.get('nombre', '')
    equipo = request.GET.get('equipo', '')
    edad_min = request.GET.get('edad_min')
    edad_max = request.GET.get('edad_max')
    puntos_min = request.GET.get('puntos_min')
    puntos_max = request.GET.get('puntos_max')
    tries_min = request.GET.get('tries_min')
    tries_max = request.GET.get('tries_max')
    orden = request.GET.get('orden', 'nombre')

    # Aplicar filtros
    if nombre:
        jugadores = jugadores.filter(nombre__icontains=nombre)
    if equipo:
        jugadores = jugadores.filter(equipo__icontains=equipo)
    if edad_min:
        jugadores = jugadores.filter(edad__gte=edad_min)
    if edad_max:
        jugadores = jugadores.filter(edad__lte=edad_max)
    if puntos_min:
        jugadores = jugadores.filter(puntos__gte=puntos_min)
    if puntos_max:
        jugadores = jugadores.filter(puntos__lte=puntos_max)
    if tries_min:
        jugadores = jugadores.filter(tries__gte=tries_min)
    if tries_max:
        jugadores = jugadores.filter(tries__lte=tries_max)

    # Ordenar
    if orden:
        jugadores = jugadores.order_by(orden)

    contexto = {
        'jugadores': jugadores,
        'nombre': nombre,
        'equipo': equipo,
        'edad_min': edad_min,
        'edad_max': edad_max,
        'puntos_min': puntos_min,
        'puntos_max': puntos_max,
        'tries_min': tries_min,
        'tries_max': tries_max,
        'orden': orden,
    }

    return render(request, 'rugby/lista_rugby.html', contexto)
