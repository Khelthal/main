Característica: Eliminar usuario
    Como administrador del sistema
    Quiero eliminar un usuario al sistema
    Para que ya no pueda utilizar el sistema

    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/administracion/usuarios/lista"
        Y inicio sesión con el usuario "juveadmin" y contraseña "123456"
        Y hago clic en Iniciar sesión
        Y presiono el botón Eliminar de la fila del usuario "kike2"
        Cuando hago clic en Confirmar
        Entonces puedo ver que el usuario "kike" ya no se encuentra en la tabla de usuarios