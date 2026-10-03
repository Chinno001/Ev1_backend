# API REST - Sistema de Diario Personal

Este proyecto es una API REST desarrollada con **Django** y **Django REST Framework (DRF)** correspondiente a las asignaturas de BackEnd. Permite gestionar entradas de diario y comentarios mediante un CRUD completo, persistencia de datos en MySQL y configuración mediante variables de entorno.

---

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework Web:** Django 6.x
* **API REST:** Django REST Framework
* **Base de Datos:** MySQL
* **Gestión de Entorno:** python-decouple

---

## Requisitos Previos

* Python 3.10+ instalado.
* Servidor MySQL en ejecución (ej. mediante XAMPP, Workbench o servicio local).
* Git instalado.

---

## Estructura del Proyecto

```text
Ev1_backend/
├── diario/                # Aplicación principal del diario
├── backend_project/       # Configuración principal de Django (settings, urls, etc.)
├── .env.example           # Plantilla de variables de entorno
├── .gitignore             # Archivos excluidos de Git
├── manage.py              # Script de gestión de Django
├── README.md              # Documentación del proyecto
└── requirements.txt       # Dependencias del proyecto