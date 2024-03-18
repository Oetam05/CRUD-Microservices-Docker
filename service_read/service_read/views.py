from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Persona
from .serializers import PersonaSerializer
import requests
import threading


class Read(APIView):
    def get(self, request, tipo, nro):
        try:
            persona = Persona.objects.get(tipo_documento=tipo,
                                          nro_documento=nro)
            serializer = PersonaSerializer(persona)
            log_data = {
                "tipo_documento": tipo,
                "nro_documento": nro,
                "action": "READ"
            }
            thread = threading.Thread(
                target=self.send_log, args=(log_data,))
            thread.start()
            return Response(serializer.data)
        except Persona.DoesNotExist:
            return Response({"error": "Persona no encontrada"},
                            status=status.HTTP_404_NOT_FOUND)


    def send_log(self, data):
        requests.post('http://kong:8000/log/', data=data)


class ReadAll(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)        
        return Response(serializer.data)