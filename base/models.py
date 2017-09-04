from django.db import models

# Create your models here.
class Pais(models.Model):
	## Nombre del pais
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Estado(models.Model):
	## Nombre del estado
	nombre = models.CharField(max_length=50)

	## Pais donde esta el estado
	pais = models.ForeignKey(Pais)

	def __str__(self):
		return self.nombre

class Municipio(models.Model):
	## Nombre del municipio
	nombre = models.CharField(max_length=50)

	## Estado donde esta el municipio
	estado = models.ForeignKey(Estado)
	def __str__(self):
		return self.nombre

class Parroquia(models.Model):
	## Nombre de la parroquia
	nombre = models.CharField(max_length=50)

	## Municipio donde esta la porroquia
	municipio = models.ForeignKey(Municipio)
	def __str__(self):
		return self.nombre

class Ciudad(models.Model):
	## Nombre de la ciudad
	nombre = models.CharField(max_length=50)

	## Estado donde esta la ciudad
	estado = models.ForeignKey(Estado)
	def __str__(self):
		return self.nombre
