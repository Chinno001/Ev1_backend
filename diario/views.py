# Django imports para crear vistas y manejar solicitudes HTTP
from django.shortcuts import render # Este módulo es pa renderizar plantillas HTML y devolverlas como respuestas HTTP. Permite pasar datos desde la vista a la plantilla.
from django.contrib.auth.decorators import login_required #Decorator, para exigir el inicio de sesión
from django.contrib.auth.mixins import LoginRequiredMixin #Mixin, para exigir el inicio de sesión
from django.http import HttpResponse #Este módulo permite devolver respuestas HTTP desde las vistas. (Contenido HTML, JSON, etc.)
from django.views import View #Clase base para crear vistas basadas en clases en Django. Permite definir métodos como get() y post() para manejar solicitudes HTTP específicas.


# Create your views here. #Acá abajo agregaré las vistas que se van a usar en la aplicación "diario". Son funciones o clases que reciben solicitudes HTTP y devuelven respuestas HTTP. Pueden renderizar plantillas HTML, procesar formularios, interactuar con la base de datos, etc. 

# > Vista pública de bienvenida (la que van a ver todos) <

def vista_bienvenida(frozen): #frozen es para que no se pueda modificar la variable, buena práctica para evitar errores (la bienvenida no se modifica).
    return HttpResponse("Bienvenidx a la vista pública del sistema Diario Personal!")

# > Vista protegida (basada en funciones FBV) <

@login_required(login_url='/admin/login/') #<-- Aquí debe ir la ruta de inicio de sesión, en este caso la del admin
def vista_protegida_funcion(request):
    return HttpResponse(f"Hola {request.user.username}, solo tu tienes acceso a esta vista protegida por función, bien hecho.")

# > Vista protegida pero ahora basada en clases (CBV) <

class VistaProtegidaClase(LoginRequiredMixin, View):
    login_url = '/admin/login/' #Redirige si no está autenticado

    def get(self, request):
        return HttpResponse(f"Hola {request.user.username}, tienes acceso a esta vista protegida por clase, bien hecho de nuevo.")