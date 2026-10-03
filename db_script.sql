#Una base de datos en entornos profesionales debe controlarse con usuarios específicos con permisos otorgados explícitamente.
#Esto lo lograremos ejecutando sentencias SQL directamente en el motor de DB, de la siguiente forma:


-- Crear la base de datos
CREATE DATABASE mi_base_datos;

-- Crear usuario remoto con contraseña
CREATE USER 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';

-- Otorgar privilegios sobre la base de datos al usuario
GRANT ALL PRIVILEGES ON mi_base_datos.* TO 'Usuario'@'%';

-- Aplicar los cambios de permisos
FLUSH PRIVILEGES;