from django.shortcuts import render
from django.views.generic import View
from .models import *

class BebederosListView(View):
	def get(self, request):
		template_name = "bebederos/bebederosList.html"

		bebederos = Bebedero.objects.all().order_by('modelo')
		context = {
			'bebederos': bebederos
		}
		return render(request, template_name, context)