# Library-with-Django


<img src = "img/libreria.png" alt = "Libreria">
Librería Django
Librería Django es una aplicación web que permite gestionar una librería online. Con esta aplicación, puedes crear, editar, borrar y consultar libros, autores, géneros y editoriales. También puedes realizar préstamos y devoluciones de libros, y ver el historial de tus operaciones.

## Características


Utiliza el framework Django para el desarrollo web.
Usa SQLite como base de datos.
Implementa el patrón de diseño MVC (Modelo-Vista-Controlador).
Tiene una interfaz de usuario sencilla y amigable.
Incluye autenticación de usuarios y permisos de acceso.
Tiene pruebas unitarias y de integración.

## Requisitos
- Python 3.9 o superior
- Django 3.2 o superior
- Pipenv o virtualenv
- Instalación
- Clona este repositorio en tu máquina local.
- Crea un entorno virtual con Pipenv o virtualenv e instala las dependencias.
- Ejecuta las migraciones para crear la base de datos.
- Crea un superusuario para acceder al panel de administración.
- Ejecuta el servidor de desarrollo.
- git clone git@github.com:Victor050106/Library-with-Django.git
- cd libreria-django
- pipenv install
- pipenv shell
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver


## Uso

- Abre tu navegador y visita http://localhost:8000/ para ver la página principal de la librería.
- Haz clic en los enlaces para navegar por las distintas secciones de la aplicación.
- Usa el botón de iniciar sesión para acceder con tu usuario y contraseña.
- Si eres superusuario, puedes acceder al panel de administración en http://localhost:8000/admin/ para gestionar los modelos de la aplicación.

## Contribuir

 Si quieres contribuir a este proyecto, puedes hacerlo de las siguientes formas:

- Reportar errores o sugerir mejoras en la sección de issues.
- Enviar pull requests con tus cambios o nuevas funcionalidades.
- Escribir o mejorar la documentación del proyecto.
- Compartir el proyecto con otros usuarios interesados.

## Author
- @Victor050106
## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.