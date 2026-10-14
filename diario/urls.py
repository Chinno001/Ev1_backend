from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #Esto es para poder usar las vistas de autenticación de Django, como login y logout, que ya vienen implementadas y listas para usar mu weno.

#Aquí se definen las rutas URL para la aplicación "diario". Cada ruta está asociada a una vista específica alojada en views.py
urlpatterns = [
    path('', views.vista_bienvenida, name='vista_bienvenida'), #Vista pública de bienvenida
    path('protegida-funcion/', views.vista_protegida_funcion, name='vista_protegida_funcion'), #Vista protegida basada en funciones
    path('protegida-clase/', views.VistaProtegidaClase.as_view(), name='vista_protegida_clase'), #Vista protegida basada en clases 
]