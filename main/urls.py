from django.conf.urls import url
from . import views

app_name = "main"
urlpatterns = [
	url(r'^contacto/$', views.Contacto.as_view(),name="contacto"),
	url(r'^$', views.Home.as_view(),name="home"),
]