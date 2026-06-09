from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    confirmados = models.IntegerField(default=0)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return self.titulo