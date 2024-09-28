Descripción del problema

El problema radica en diseñar y desarrollar un software de gestión de tareas que permita a los usuarios organizar y realizar un seguimiento de su trabajo de forma eficaz. El software debe proporcionar una interfaz fácil de usar que permita a los usuarios crear, editar y gestionar sus tareas, así como generar informes en formato PDF. Este software es ideal para aquellos que necesitan organizar muchas tareas y mantenerse ordenados, como estudiantes, profesionales y cualquier persona que quiera priorizar y controlar sus actividades diarias. El software permitirá a los usuarios crear cuentas, cambiar contraseñas, iniciar sesión y crear tareas con título, descripción, fecha límite y prioridad. Asimismo, podrán editar la información de una tarea, crear categorías de tareas, agrupar tareas por categorías y eliminar tareas existentes. Además, el programa generará informes en PDF con las tareas del usuario agrupadas por categoría.
El propósito de este software de gestión de tareas es ayudar a los usuarios a mantenerse organizados y enfocados, proporcionando una plataforma centralizada para gestionar sus tareas. Con el objetivo de aumentar la productividad, reducir el estrés y proporcionar una visión clara de las tareas y sus fechas limite. El software igualmente permitirá a los usuarios rastrear su progreso, identificar áreas de mejora y tomar decisiones informadas sobre la gestión de sus tareas.


Análisis del problema

El proyecto busca crear un software para que los usuarios puedan organizar y supervisar sus tareas de manera eficiente. A continuación, se detallan las funciones necesarias para el proyecto. El proyecto debe incluir funciones básicas como registrarse, iniciar sesión, cambiar la contraseña y crear tareas con información relevante como título, descripción, fecha límite y prioridad. Además, los usuarios pueden editar, crear categorías, agrupar y eliminar tareas. Igualmente, el programa debe poder crear informes en formato PDF con la lista de tareas de un usuario ordenadas por categorías.


Requisitos funcionales


Nombre	RF1 – Crear Cuenta de Usuario
Resumen	El sistema permitirá a los usuarios nuevos registrarse en la aplicación proporcionando un nombre de usuario y una nueva contraseña
Entradas
Nombre de Usuario
Contraseña
Resultado	
1.	Registro realizado apropiadamente
1.1 La cuenta es creada correctamente
2.	El sistema redirige al usuario a una pantalla de bienvenida o a su perfil recién creado

Pasos	Métodos	Responsabilidades

Ingresar un nombre de usuario	ingresar_nombre_usuario(nombre_usuario: str)	Usuario
Ingresar una contraseña	ingresar_contraseña(contraseña: str)	Usuario
Validar el nombre de usuario	Validar_nombre_usuario(nombre_usuario: str)	Sistema
Validar la contraseña	validar_contraseña(contraseña: str)	Sistema
Guardar la nueva contraseña	crear_cuenta_usuario(nombre_usuario: str, contraseña: str)	Usuario
Confirmar la creación de la cuenta	confirmar_creacion_cuenta(nombre_usuario: str)	Sistema
Redirigir al usuario a la pantalla de bienvenida o perfil	redirigir_a_perfil()	Sistema


Nombre	RF2 – Cambiar Contraseña
Resumen	El sistema permitirá a los usuarios cambiar su contraseña actual por una nueva
Entradas
Contraseña actual
Nueva contraseña
Confirmación de nueva contraseña
Resultado	
1.	La contraseña es cambiada correctamente
2.	El sistema notifica al usuario sobre el éxito del cambio 
3.	El usuario es redirigido a la pantalla de su perfil

Pasos	Métodos	Responsabilidades
Ingresar contraseña actual	ingresar_contraseña_actual(contraseña_actual: str)	Usuario
Ingresar una nueva contraseña	ingresar_nueva_contraseña(contraseña_nueva: str)	Usuario
Confirmar la nueva contraseña	confirmar_contraseña(confirmar: str)	Usuario
Validar la contraseña actual.	validar_contraseña_actual(contraseña_actual: str)	Sistema
Validar la nueva contraseña	validar_nueva_contraseña(contraseña_nueva: str)	Sistema
Cambiar la contraseña	cambiar_contraseña(contraseña_actual: str, contraseña_nueva: str)	Usuario
Confirmar el cambio de contraseña.	confirmar_cambio_contraseña()	Sistema
Redirigir al usuario a su perfil.	redirigir_a_perfil()	Sistema


Nombre	RF3 – Iniciar Sesión 
Resumen	El sistema permitirá a los usuarios iniciar sesión proporcionando su nombre de usuario y contraseña
Entradas
Nombre de usuario 
Contraseña
Resultado	
1.	El usuario es autenticado correctamente
2.	El sistema redirige al usuario a su panel de control o página principal
3.	Si las credenciales son incorrectas, se muestra un mensaje de error


Pasos	Métodos	Responsabilidades
Ingresar nombre de usuario.	ingresar_nombre_usuario(nombre_usuario: str)	Usuario
Ingresar contraseña.	ingresar_contraseña(contraseña: str)	Usuario
Validar las credenciales	validar_credenciales(nombre_usuario: str, contraseña: str)	Sistema
Si las credenciales son correctas, autenticar al usuario.	autenticar_usuario(nombre_usuario: str)	sistema
Redirigir al usuario a su perfil o pagina principal	redirigir_a_perfil()	Sistema
Si las credenciales son incorrectas, mostrar un mensaje de error	mostrar_mensaje_error()	Sistema


Nombre	RF4 – Crear Tarea 
Resumen	El sistema permitirá a los usuarios, una vez que la sesión esta iniciada, crear una tarea proporcionando un título, una descripción, una fecha limite y una prioridad
Entradas
Titulo
Descripción
Fecha limite
Prioridad
Resultado	
1.	La tarea es creada correctamente
2.	El sistema notifica al usuario sobre el éxito de la creación de la tarea
3.	La nueva tarea se muestra en la lista de tareas del usuario 

Pasos	Métodos	Responsabilidades
Ingresar un título para la tarea	ingresar_titulo(título: str)	Tareas
Ingresar descripción para la tarea	Ingresar_descripcion(descripción: str)	Tareas
Ingresar fecha limite	Ingresar_fecha_limite(fecha_limite: str)	Tareas
Seleccionar prioridad	Ingresar_prioridad(prioridad: str)	Tareas
Validar los datos ingresados	validar_datos_tarea(título: str, descripción: str, fehca_limite: str, prioridad: str)	Tareas
Crear la nueva tarea	crear_tarea(título: str, descripción: str, fehca_limite: str, prioridad: str)	Tareas
Confirmar la creación de la tarea	Confirmar_creacion_tarea()	Sistema
Mostrar la nueva tarea en la lista	mostrar_tarea(tarea_id: int)	Sistema


Nombre	RF5 – Editar tarea 
Resumen	El sistema permitirá a los usuarios editar la información de una tarea existente, incluyendo el título, la descripción, la fecha limite y la prioridad
Entradas
ID de la tarea
Titulo
Descripción
Fecha limite
Prioridad 
Resultado	
1.	La tarea es editada correctamente
2.	El sistema notifica al usuario sobre el éxito de la edición de la tarea
3.	La tarea editada se muestra en la lista de tareas del usuario 

Pasos	Métodos	Responsabilidades
Seleccionar la tarea a editar	seleccionar_tarea(tarea_id: int)	Usuario
Ingresar un nuevo titulo	ingresar_nuevo_titulo(título: str)	Tareas
Ingresar una nueva descripción	ingresar_nueva_descripcion(descripción: str)	Tareas
Ingresar una nueva fecha límite	ingresar_nueva_fecha_limite(fecha_limite: str)	Tareas
Seleccionar nueva prioridad	ingresar_nueva_prioridad(prioridad: str)	Tareas
Validar los nuevos datos	validar_datos_tarea(tarea_id: int, título: str, descripción: str, fecha_limite: str, prioridad: str)	Tareas
Editar la tarea	editar_tarea(tarea_id: int, título: str, descripción: str, fecha_limite: str, prioridad: str)	Tareas
Confirmar la edición de la tarea	confirmar_edicion_tarea()	Sistema
Mostrar la tarea editada en la lista	mostrar_tarea(tarea_id: int)	Sistema


Nombre	RF6 – Crear Categorías 
Resumen	El sistema permitirá a los usuarios crear categorías para organizar sus tareas. Cada categoría debe tener un nombre y una descripción 
Entradas
Nombre de la categoría
Descripción de la categoría 
Resultado	
1.	La categoría es creada correctamente
2.	El sistema notifica al usuario sobre el éxito de la creación de la categoría
3.	La nueva categoría se muestra en la lista de categorías del usuario 

Pasos	Metodos	Responsabilidades
Ingresar el nombre de la categoría	ingresar_nombre_categoria(nombre: str)	Categorías
Ingresar la descripción de la categoría	ingresar_descripcion_categoria(descripcion_categoria: str)	Categorías
Validar los datos ingresados	validar_datos_categoria(nombre: str, descripcion_categoria: str)	Categorías
Crear la nueva categoría	crear_categoria(nombre: str, descripcion_categoria: str)	Categorías
Confirmar la creación de la categorial	confirmar_creacion_categoria()	Sistema
Mostrar la nueva categoría en la lista	mostrar_categoria(nombre: str)	Sistema


Nombre	RF7 – Agrupar Tareas por Categoría
Resumen	El sistema permitirá a los usuarios agrupar sus tareas en diferentes categorías, como trabajo, personal, estudio, etc. El usuario seleccionará una categoría al momento de crear o editar una tarea
Entradas	
ID de la tarea
Categoría seleccionada
Resultado	
1.	 La tarea se agrupa correctamente en la categoría seleccionada.
2.	 El sistema actualiza la lista de tareas organizadas por categoría. 
3.	 El usuario puede visualizar las tareas según la categoría seleccionada.

Pasos	Métodos	Responsabilidades
Seleccionar la tarea a agrupar	Seleccionar_tarea(tarea_id: int)	Usuario
Elegir la categoría de la tarea	seleccionar_categoria(categoría: str)	Usuario
Validar la categoría seleccionada	validar_categoria(categoria: str)	Sistema
Agrupar la tarea en la categoria seleccionada	agrupar_tarea_por_categoria(tarea_id: int, categoria: str)	Categorías
Actualizar la lista de tareas organizadas por categoría	actualizar_lista_tareas_por_categoria()	Sistema
Visualizar las tareas según la categoría seleccionada	mostrar_tareas_por_categoria(categoria: str)	Sistema


Nombre	RF8 – Eliminar Tareas
Resumen	El sistema permitirá a los usuarios eliminar tareas existentes de su lista de tareas
Entradas
ID de la tarea a eliminar
Resultado	
1.	La tarea es eliminada correctamente
2.	El sistema notifica al usuario sobre el éxito de la eliminación de la tarea
3.	La tarea es eliminada y ya no se muestra en la lista de tareas del usuario

Pasos	Métodos	Responsabilidades
Seleccionar la tarea a eliminar	seleccionar_tarea(tarea_id: int)	Usuario
Confirmar la existencia de la tarea	verificar_existencia_tarea(tarea_id: int)	Sistema
Solicitar la confirmación de eliminación	confirmar_eliminacion_tarea(tarea_id: int)	Usuario
Eliminar la tarea seleccionada	eliminar_tarea(tarea_id: int)	Tareas
Confirmar la eliminación al usuario	notificar_eliminacion()	Sistema
Actualizar la lista de tareas	actualizar_lista_tareas()	Sistema


Nombre	RF9 – Generar Informe de Tareas en PDF
Resumen	El sistema permitirá generar un informe en formato PDF con la lista de tareas de un usuario, agrupadas por categorías
Entradas
ID del usuario
Lista de tareas del usuario agrupadas por categorías
Resultado	
1. Se genera un archivo PDF con las tareas del usuario agrupadas por categorías
2.	El sistema notifica al usuario sobre la finalización del proceso de generación del informe
3.	El archivo PDF esta disponible para su descarga o visualización 

Pasos	Métodos	Responsabilidades
Solicitar generar un informe en PDF	solicitar_informe_pdf(usuario_id: int)	Usuario
Obtener la lista de tareas del usuario agrupadas por categorías	obtener_tareas_por_categoria(usuario_id: int)	Sistema
Generar el archivo PDF con las tareas	generar_pdf(tareas: dict, usuario_id: int)	Sistema
Notificar al usuario que el PDF ha sido generado	notificar_generacion_pdf()	Sistema
Poner el PDF a disposición del usuario	poner_disponible_pdf(usuario_id: int)		Sistema
Descargar o visualizar el informe PDF	descargar_pdf(usuario_id: int)	Usuario
