from django.contrib import admin
from .models import Entrada, Comentario

# Register your models here.
admin.site.register(Entrada) #Registro de la clase Entrada en el panel de administración de Django.
admin.site.register(Comentario) #Registro de la clase Comentario en el panel de administración de Django.