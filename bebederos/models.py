from django.db import models

class Bebedero(models.Model):
	nivel_educativo_choices = (
		('Preescolar','Preescolar'),
		('Primaria','Primaria'),
		('Secundaria','Secundaria'),
	)
	modelo = models.CharField(max_length=30)
	rango_usuarios = models.CharField(max_length=30)
	foto = models.ImageField(upload_to="bebederos")
	nivel_educativo = models.CharField(max_length=30, choices=nivel_educativo_choices)

	def __str__(self):
		return self.modelo
