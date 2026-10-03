from django.db import models
import datetime

#ahora = datetime.datetime.now() #Variante creada para evitar error en la línea created_at = models.DateTimeField(default=ahora)

# Create your models here.

#Aquí abajo se definen las clases(MiClase y MiClase2) que representan las tablas en la base de datos.

class Entrada(models.Model):
    id_entrada = models.AutoField(primary_key=True) #AutoField, campo de clave primaria, se autoincrementa automáticamente.
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE) #ForeignKey, campo de clave foránea, se relaciona con la tabla auth_user de Django.
    titulo = models.CharField(max_length=100) #Charfield, texto corto, max_length=100
    contenido = models.TextField(null=False) #TextField sin limite, para que el usuario pueda escribir un contenido más largo. 
    fecha_creacion = models.DateTimeField(null=False) #Fecha y hora de la creación de la entrada.
    visibilidad = models.BooleanField(default=True) #Público o privado según decida el usuario.
    estado = models.CharField(max_length=100,null=False) #Habilitado o deshabilitado según decida el usuario.
    categoria = models.CharField(max_length=100,null=False) #Categoría de la entrada según decida el usuario.
    class Meta:
            db_table_comment = "Tabla de las entradas creadas por los usuarios."
    #autor = models.CharField(max_length=25,null=False) #Charfield, texto corto, max_length=25, null=False indica que no puede ser nulo.
    #contenido = models.TextField(max_length=100,null=False) #TextField, texto largo, max_length=100, null=False indica que no puede ser nulo.
    #fecha_hora = models.DateTimeField(max_length=100,null=False) #DateTimeField, fecha y hora, max_length=100, null=False indica que no puede ser nulo.
    #fecha = models.DateField(null=False) #DateField, fecha, null=False indica que no puede ser nulo.
    #hora = models.TimeField(null=False) #TimeField, hora, null=False indica que no puede ser nulo.
    #atributo_6 = models.IntegerField() #IntegerField, número entero.
    #atributo_7 = models.DecimalField() #Decimalfield, número decimal.
    #atributo_8 = models.FloatField() #FloatField, número decimal de punto flotante.
    #atributo_9 = models.EmailField() #EmailField, campo de correo electrónico, validará que el valor ingresado sea un correo electrónico válido.
    #atributo_10 = models.BooleanField(default=True) #Booleano de toda la vida, verdadero o falso.
    #atributo_11 = models.URLField(default=True) #URLField, campo de URL, validará que el valor ingresado sea una URL válida.
    #created_at = models.DateTimeField(default=ahora) 
    #updated_at = models.DateTimeField(auto_now=True) 

class Comentario(models.Model):
    #atributo_referenciado = models.ForeignKey(Entrada,on_delete=models.CASCADE) #El parámetro on_delete=models.CASCADE indica qué ocurre al eliminar el registro padre: si se elimina el registro padre, también se eliminarán los registros hijos asociados. 
    contenido = models.CharField(max_length=100) 
    fecha_hora = models.DateTimeField(max_length=100,null=False)
    autor = models.CharField(max_length=25,null=False)
    class Meta:
        db_table_comment = "Tabla de los comentarios creados por los usuarios."