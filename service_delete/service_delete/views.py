from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Persona
import requests, threading

class Delete(APIView):
    def delete(self, request, tipo, nro):
        try:
            persona = Persona.objects.get(tipo_documento=tipo,
                                          nro_documento=nro)
            persona.delete()
            log_data = {
                "tipo_documento": tipo,
                "nro_documento": nro,
                "action": "DELETE"
            }            
            thread = threading.Thread(
                target=self.send_log, args=(log_data,))
            thread.start()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Persona.DoesNotExist:
            return Response({"error": "Persona no encontrada"},
                            status=status.HTTP_404_NOT_FOUND)

    def send_log(self, data):
        requests.post('http://kong:8000/log/', data=data)
