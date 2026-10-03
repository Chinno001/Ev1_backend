# La librería rest_framework que instalamos anteriormente, tiene la herramienta para
# serializar nuestro modelo de datos en formato JSON,
# lo que lograremos siguiendo estos pasos:

# Primero crearemos un archivo serializer.py en el directorio de nuestra aplicación.
# En el archivo creado, importaremos serializers para usarlos en la serialización de nuestro modelo.
# Junto con esto, debemos importar todo nuestro modelo de datos desde models.py.
# Finalmente, crearemos una clase que se encargará de serializar cada uno de nuestros modelos de datos.

from rest_framework import serializers

from .models import Entrada
from .models import Comentario

class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fileds = ('__all__')
        # __'all__' serializa todos los atributos de la clase/modelo.

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fileds = ('__all_')
        #También hubiera podido ser:
        #fileds = ('atributo_referenciado','atributo_2')
        #Esto para poder Decidir qué atributos de nuestra clase/modelo serializamos.