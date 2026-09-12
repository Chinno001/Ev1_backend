from django.shortcuts import render

# Create your views here. #Acá se alojan las 'Vistas' o lo que el sistema mostrará. En este caso agregué el html 'bienvenida'.
def bienvenida(request):
    return render(request, 'diario/bienvenida.html')