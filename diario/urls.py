from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'), #Esto llama a la vista (sin la ruta)
]