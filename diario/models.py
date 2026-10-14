from django.db import models
import datetime


# Create your models here.

#Aquí abajo se definen las clases(Entrada, Comentario) que representarán las tablas en la base de datos.

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

class Comentario(models.Model):
    #atributo_referenciado = models.ForeignKey(Entrada,on_delete=models.CASCADE) #El parámetro on_delete=models.CASCADE indica qué ocurre al eliminar el registro padre: si se elimina el registro padre, también se eliminarán los registros hijos asociados. 
    contenido = models.CharField(max_length=100) 
    fecha_hora = models.DateTimeField(max_length=100,null=False)
    autor = models.CharField(max_length=25,null=False)
    class Meta:
        db_table_comment = "Tabla de los comentarios creados por los usuarios."
