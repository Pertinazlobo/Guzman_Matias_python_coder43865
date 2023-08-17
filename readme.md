Autor : Matias Guzmán

Nombre del proyecto

Pagina para uso interno de ventas de libros, comics etc.

Descripción sobre el proyecto

Este preoyecto se realizo para cualquier local de ventas de libros, la app cuenta con la alta, baja, modificación y borrado de libros, clientes y compras. Los datos persisten en una base de datos de Sqlite3.

Inicio
.Abrir la carpeta donde se encuentra el proyecto y desde ahi abrir la consola de comandos(CMD).
.Levantar el servidor usando el comando python manage.py runserver
.Entrar desde algun navegador de internet a la direccion IP que nos provee el runserver(por default 127.0.0.1:8000) y despues de la direccion IP librosapp/

Caracteristicas
.El proyecto cuenta con una pagina de inicio donde el usuario debe registrarse para poder empezar a utilizar la aplicacion.
.Una ves ingresado al sistema el usuario tiene acceso a cinco secciones compras, libros, Clientes, Editar Perfil y agregar Avatar.
-Dentro de la seccion Compras se puede realizar la venta del los libros previamente teniendo cargado en la base de datos los datos de los mismos y los datos del cliente, tambien en caso de equivocarse con la compraa se puede modificar o eliminar.
-Dentro de la seccion Cliente se puede cargar los datos del cliente, nombre, apellido y email, tambien en caso de algun error de carga de los datos o que el cliente ya no compre mas se puede modificar o eliminar.
-Dentro de la seccion Editar Perfil, se puede modificar los datos del usuario que utiliza la aplicacion.
-Dentro de la seccion de Agregar avatar, el usuario puede cargar una foto propia o avatar preestablecido.

En la pagina principal se encuentra los botones de login, registro y admin, a este ultimo solo el administrador de sitio puede acceder. En caso de tener un usuario y contraseña se podra loguear a la pagina, de no contar con un usuario podra registrarse, el registro le solicitara Usuario, Nombre, Apellido, email y contraseña.
2.Una ves logueado, dentro de la pagina ya se encuentran cargados datos de libros, compras y clientes, pero si se quiere cargar algun libro o cliente nuevo, dentro de Libros podra cargar los datos de los mismos y dentro de cliente podra cargar los datos de nuevo cliente.
3.Para realizar una busqueda de una compra,ingresa al boton Compra y tiene la info de la compra para modificar o barrar la misma.
4.Desde la Opcion admin se puede manejar toda la base de datos, el "usuario" es admin y la "password" es admin123456.
5.Se creo un usuario de prueba, el "usuario" es Matias y la "password" es \*coderhouse

. Para este proyecto se desarrollaron la siguiente App
-Librosapp

2. Dentro de la App librosapp se desarrollo los siguientes Models
   class Cliente
   class Compra
   class Libro

   Y Se desarrollo las siguientes Views
   class AgregarLibroView
   class BuscarLibroView
   class ActualizarLibroView
   class BorrarLibroView
   class AgregarClienteView
   class BuscarClienteView
   class ActualizarClienteView
   class BorrarClienteView
   class AgregarCompraView
   class BuscarCompraView
   class ActualizarCompraView
   class BorrarCompraView

3. Dentro de la App Librosapp se desarrollo los siguientes Models
   class Avatar

   Y Se desarrollo las siguientes Views
   def login_request
   def register
   class EditarPerfilView
   class AgregarAvatarView
