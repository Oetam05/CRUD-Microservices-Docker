from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Persona
from .serializers import PersonaSerializer
import requests
import threading


class Update(APIView):
    def put(self, request, tipo, nro):
        try:
            persona = Persona.objects.get(
                tipo_documento=tipo, nro_documento=nro)
        except Persona.DoesNotExist:
            return Response({"error": "Persona no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            log_data = {
                "tipo_documento": tipo,
                "nro_documento": nro,
                "action": "UPDATE"
            }
            thread = threading.Thread(
                target=self.send_log, args=(log_data,))
            thread.start()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_log(self, data):
        requests.post('http://kong:8000/log/', data=data)
