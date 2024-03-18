from django.db import models

class Log(models.Model):
    class Meta:
        app_label = 'logs'
    timestamp = models.DateTimeField(auto_now_add=True)    
    action = models.CharField(max_length=255)
    tipo_documento = models.CharField(
        max_length=30, choices=[("TI", "Tarjeta de Identidad"), ("CC", "Cédula")])
    nro_documento = models.CharField(
        max_length=10)
