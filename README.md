# Evaluacion-5-Django

## En esta evaluación usted tendrá la responsibilidad de habilitar en el
framerowk Django el sistema para apoyo de seguimiento médico de
pacientes, que fué objeto de estudio en la evaluación del módulo 1 de
este curso. [Ir](https://pcidsoto.github.io/Evaluacion-Modulo-1/)

## ¿Qué servidor HTTP cree apropiado para desplegar su aplicación en producción? ¿Cómo se debe realizar el despliegue del proyecto Django?

- Servidor Apache HTTP, lo escogemos por ser de código abierto y porque puede instalarse en casi todos los sistemas operativos.
Utilizando WSGI desplegaremos nuestro proyecto.
En vez de usar el python manage.py runserver, levantamos el servidor con Apache, virtualhost y configuramos para abrir otros puertos.

## Grupo 3 - Full Stack Python - Awakelab

## Accesso
- Restaurar base de datos sinars.sql que está en la carpeta db.

- De lo contrario Crear base de datos en postgres como sinars
- Hacer python manage.py migrate
- Crear superusuario 
- Iniciar el servidor
- ir a localhost:8000/admin, ingresar y agregar los campos faltantes del admin( nombre, apellido, etc )
- crear un usuario como paciente
- agregar datospersonales y datos como examenes, etc.
- luego probar los usuarios en el directorio default de la aplicación.

## Nota: 
### ESTADO DE LA APP EN DESARROLLO 
- SOLO SE PUEDE VISUALIZAR INFORMACION DEL PACIENTE.
- DESDE LA INTEFAZ DE CLIENTE SOLO EL ADMIN PUEDE AGREGAR Y ELIMINAR PACIENTES.
- LOS OTROS ROLES COMO FAMILIAR, MEDICO, CUIDADOR ESTÁ SIN DESARROLLAR POR LO QUE POSIBLEMENTE LA APP MUESTRE ERRORES SI INTENTA CREAR UN USUARIO DE ESE TIPO.
- PARA AGREGAR DATOS DE PRUEBA IR AL SITIO DE ADMINISTRACION PROPORCIONADO POR DJANGO localhost:8000/admin
 

### Usuario - Contraseña
#### admin -> admin 1234
### paciente de prueba -> alan 1234

