from django.db import models
import re
from django.forms import ValidationError


def validar_doc(value):
    pattern = re.compile(r"^\d{4,10}$")
    if not pattern.match(value):
        raise ValidationError("Nro de documento invalido")


def validar_cel(value):
    pattern = re.compile(r"^\d{10}$")
    if not pattern.match(value):
        raise ValidationError("Celular debe tener 10 digitos")


class Persona(models.Model):
    class Meta:
        app_label = 'personas'
    tipo_documento = models.CharField(
        max_length=30, choices=[("TI", "Tarjeta de Identidad"), ("CC", "Cédula")])
    nro_documento = models.CharField(
        max_length=10, unique=True, validators=[validar_doc])
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=20, choices=[(
        "M", "Masculino"), ("F", "Femenino"), ("NB", "No binario"), ("NR", "Prefiero no reportar")])
    correo_electronico = models.EmailField()
    celular = models.CharField(max_length=10, validators=[validar_cel])
    foto = models.ImageField(upload_to="fotos/", max_length=100)

    def __str__(self):
        return self.primer_nombre
