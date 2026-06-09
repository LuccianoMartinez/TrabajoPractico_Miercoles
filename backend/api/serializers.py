from rest_framework import serializers
from .models import Evento

class EventoSerializer(serializers.ModelSerializer):
    disponible = serializers.SerializerMethodField()
    
    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descripcion', 'fecha', 'ubicacion', 
                  'capacidad', 'confirmados', 'disponible', 'creado_en']
    
    def get_disponible(self, obj):
        return obj.capacidad - obj.confirmados