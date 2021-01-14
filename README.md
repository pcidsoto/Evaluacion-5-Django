# Evaluacion-5-Django

## En esta evaluación usted tendrá la responsibilidad de habilitar en el
framerowk Django el sistema para apoyo de seguimiento médico de
pacientes, que fué objeto de estudio en la evaluación del módulo 1 de
este curso. [a link](https://pcidsoto.github.io/Evaluacion-Modulo-1/)

## ¿Qué servidor HTTP cree apropiado para desplegar su aplicación en producción? ¿Cómo se debe realizar el despliegue del proyecto Django?

- Servidor Apache HTTP, lo escogemos por ser de código abierto y porque puede instalarse en casi todos los sistemas operativos.
Utilizando WSGI desplegaremos nuestro proyecto.
En vez de usar el python manage.py runserver, levantamos el servidor con Apache, virtualhost y configuramos para abrir otros puertos.

##Grupo 3 - Full Stack Python - Awakelab
