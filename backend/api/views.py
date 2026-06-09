from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Evento
from .serializers import EventoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    
    @action(detail=True, methods=['post'])
    def confirmar_asistencia(self, request, pk=None):
        evento = self.get_object()
        if evento.confirmados < evento.capacidad:
            evento.confirmados += 1
            evento.save()
            return Response({'status': 'asistencia confirmada'})
        return Response({'error': 'evento lleno'}, status=400)
    
    @action(detail=True, methods=['post'])
    def cancelar_asistencia(self, request, pk=None):
        evento = self.get_object()
        if evento.confirmados > 0:
            evento.confirmados -= 1
            evento.save()
            return Response({'status': 'asistencia cancelada'})
        return Response({'error': 'no hay asistencias para cancelar'}, status=400)