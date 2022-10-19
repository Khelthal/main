Característica: Agregar usuario
    Como administrador del sistema
    Quiero agregar un usuario al sistema
    Para que pueda utilizar el sistema

    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/administracion/usuarios/nuevo"
        Y inicio sesión con el usuario "juveadmin" y contraseña "123456"
        Y hago clic en Iniciar sesión
        Y agrego los valores de nombre: "kike", contraseña: "123456" y correo: "kike@gmail.com"
        Cuando hago clic en Guardar
        Entonces puedo ver al usuario "kike" en la lista de usuarios