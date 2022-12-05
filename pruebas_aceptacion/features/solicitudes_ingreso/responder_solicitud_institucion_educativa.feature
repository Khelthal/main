Característica: Responder solicitud de una institución educativa
	Como administrador
	Quiero reponder la solicitud de una institución educativa
	Para que se genere su perfil o se elimine su solicitud

	Escenario: Aprobar solicitud
        Dado que existe una solicitud de una institución educativa llamada "prueba-institucion"
        Y que ingreso al sistema en el dominio "/administracion/instituciones_educativas/solicitud"
        Y inicio sesión como administrador con el usuario "root" y contraseña "prueba"
        Y busco el registro de "prueba-institucion"
        Cuando hago clic en la opción "aprobar"
        Entonces se muestra el registro de "prueba-institucion"
	
	Escenario: Rechazar solicitud
	Dado que existe una solicitud de una institución educativa llamada "prueba-institucion"
        Y que ingreso al sistema en el dominio "/administracion/instituciones_educativas/solicitud"
        Y inicio sesión como administrador con el usuario "root" y contraseña "prueba"
        Y busco el registro de "prueba-institucion"
        Cuando hago clic en la opción "rechazar"
        Y confirmo mi decisión
        Y me redirijo a la ruta "/administracion/instituciones_educativas/solicitud"
        Entonces no se encuentra el registro de "prueba-institucion"
