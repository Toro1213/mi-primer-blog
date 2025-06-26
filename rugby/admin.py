from django.contrib import admin
from .models import JugadorRugby

@admin.register(JugadorRugby)
class JugadorRugbyAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'equipo', 'partidos_jugados', 'tries', 'puntos')
