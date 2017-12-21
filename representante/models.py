from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from base.models import Municipio, Parroquia
from django.contrib.auth.models import User
#from base.constant import TIPO_FRENTE

# Create your models here.

class Representante(models.Model):

    nombre = models.CharField(max_length=100)

    apellido = models.CharField(max_length=100)

    cedula = models.CharField(
        max_length=9, help_text=_("Cédula de Identidad del usuario"),
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                _("Introduzca un número de cédula válido. Solo se permiten números y una longitud de 8 carácteres. Se agrega un 0 si la longitud es de 7 carácteres.")
            ),
        ]
    )

    telefono = models.CharField(
        max_length=18, help_text=_("Número telefónico de contacto con la persona"),
        validators=[
            validators.RegexValidator(
                r'^\(\+\d{3}\)-\d{3}-\d{7}$',
                _("Número telefónico inválido. Solo se permiten números y los símbolos: '(', ')', '-', '+'")
            ),
        ]
    )

    correo = models.CharField(
        max_length=100, help_text=("correo@correo.com")
    )

#class Frente(models.Model):

#    nombre = models.CharField(max_length=100, choices=TIPO_FRENTE)

#    persona = models.ForeignKey(Persona)

#    municipio = models.ForeignKey(Municipio, null=True)

#    parroquia = models.ForeignKey(Parroquia, null=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
