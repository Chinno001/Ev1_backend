from django.db import models

# Create your models here.

#Aquí abajo se definen las clases(MiClase y MiClase2) que representan las tablas en la base de datos.
#Como mi proyecto es un diario, la clase podría llamarse 'Entrada' o 'Posteo', pero para mantener un orden y no
#confundirme dejaré los ejemplos de mi profesor tal cual los dejó en el curso.

class MiClase(models.Model):
    atributo_1 = models.CharField(max_length=25,null=False) #Charfield, texto corto, max_length=25, null=False indica que no puede ser nulo.
    atributo_2 = models.TextField(max_length=100,null=False) #TextField, texto largo, max_length=100, null=False indica que no puede ser nulo.
    atributo_3 = models.DateField(null=False) #DateField, fecha, null=False indica que no puede ser nulo.
    atributo_4 = models.TimeField(null=False) #TimeField, hora, null=False indica que no puede ser nulo.
    atributo_5 = models.DateTimeField(max_length=100,null=False) #DateTimeField, fecha y hora, max_length=100, null=False indica que no puede ser nulo.
    atributo_6 = models.IntegerField() #IntegerField, número entero.
    atributo_7 = models.DecimalField() #Decimalfield, número decimal.
    atributo_8 = models.FloatField() #FloatField, número decimal de punto flotante.
    atributo_9 = models.EmailField() #EmailField, campo de correo electrónico, validará que el valor ingresado sea un correo electrónico válido.
    atributo_10 = models.BooleanField(default=True) #Booleano de toda la vida, verdadero o falso.
    atributo_11 = models.URLField(default=True) #URLField, campo de URL, validará que el valor ingresado sea una URL válida.
    created_at = models.DateTimeField(default=ahora) 
    updated_at = models.DateTimeField(auto_now=True) 

class MiClase2(models.Model):
    atributo_referenciado = models.ForeignKey(MiClase,on_delete=CASCADE) #El parámetro on_delete=models.CASCADE indica qué ocurre al eliminar el registro padre: si se elimina el registro padre, también se eliminarán los registros hijos asociados. 
    atributo_2 = models.CharField(max_length=100) 
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)