from django.shortcuts import render
from django.views.generic import View
from .models import *

class Home(View):
	def get(self, request):
		template_name = "main/home.html"
		return render(request, template_name)

class Contacto(View):
	def get(self, request):
		template_name = "main/contacto.html"
		return render(request, template_name)		