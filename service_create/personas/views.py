from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonaSerializer
import requests
import threading


class Create(APIView):
    def post(self, request, format=None):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            log_data = {
                "tipo_documento": serializer.data["tipo_documento"],
                "nro_documento": serializer.data["nro_documento"],
                "action": "CREATE"
            }

            # Llamar a la función send_log utilizando hilos
            thread = threading.Thread(
                target=self.send_log, args=(log_data,))
            thread.start()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_log(self, data):
        requests.post('http://kong:8000/log/', data=data)
