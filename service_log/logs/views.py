from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LogSerializer
from .models import Log


class Create(APIView):
    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Read(APIView):
    def get(self, request, tipo, nro):
        try:
            log = Log.objects.filter(tipo_documento=tipo,
                                      nro_documento=nro)
            serializer = LogSerializer(log, many=True)
            return Response(serializer.data)
        except Log.DoesNotExist:
            return Response({"error": "Persona no encontrada"},
                            status=status.HTTP_404_NOT_FOUND)
            
class ReadDate(APIView):
    def get(self, request, fecha):
        try:
            log = Log.objects.filter(timestamp__date=fecha)
            serializer = LogSerializer(log, many=True)
            return Response(serializer.data)
        except Log.DoesNotExist:
            return Response({"error": "No hay logs para la fecha indicada"},
                            status=status.HTTP_404_NOT_FOUND)
