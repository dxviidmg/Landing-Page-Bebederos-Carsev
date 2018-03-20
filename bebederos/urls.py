from django.conf.urls import url
from . import views

app_name = "bebederos"
urlpatterns = [
	url(r'^bebederos/$', views.BebederosListView.as_view(),name="bebederosList"),
]