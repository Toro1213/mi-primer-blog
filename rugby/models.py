from django.db import models

class JugadorRugby(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    equipo = models.CharField(max_length=100)
    partidos_jugados = models.IntegerField()
    tries = models.IntegerField()
    puntos = models.IntegerField()
    url = models.TextField(null=True, blank=True)
    imagen = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.equipo}"

