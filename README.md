El programa es la creación de una página de una librería online, llamada “Librería del bosque”

Instalación

•	Abrir la terminal de una carpeta de la pc. En ella, clonar la página haciendo: git clone <link-del-repositorio>

•	Una vez hecho, se va a descargar en la carpeta, por lo tanto, ir a esa carpeta y abrirlo con VSCode

Ejecución

•	Abrir la terminal del archivo y ejecutar la página escribiendo: python manage.py runserver

•	Acceder a la página mediante el link que te da la terminal, el cual es http://127.0.0.1:8000/

Uso

•	Una vez que accedas a la página principal, podrás navegar por las diferentes funcionalidades:

---> "libros": acá encontraras el listado de libros que vende la librería

---> "librerías": acá encontraras el listado de artículos de librería que vende la librería

---> "Best Sellers": acá veras los libros más vendidos de la librera

---> "Sucursales": donde podrás encontrar el listado de locales que hay alrededor del mundo

•	Además, podes completar diferentes formularios para actualizar el contenido de cada página utilizando las siguientes URLs:

---> http://127.0.0.1:8000/libros_form/

---> http://127.0.0.1:8000/libreria_form/

---> http://127.0.0.1:8000/bestSeller_form/

---> http://127.0.0.1:8000/sucursales_form/

Una vez completados los formularios,hace clic en "Guardar" y serás redirigido a la página principal de cada función, donde podrás ver el contenido agregado.
