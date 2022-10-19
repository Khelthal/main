Característica: Editar usuario
    Como administrador del sistema
    Quiero modificar un usuario en el sistema
    Para actualizar su información

    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/administracion/usuarios/lista"
        Y inicio sesión con el usuario "juveadmin" y contraseña "123456"
        Y hago clic en Iniciar sesión
        Y presiono el botón Editar de la fila del usuario "kike"
        Y modifico los valores a nombre: "kike2", contraseña: "123456" y correo: "kike2@gmail.com"
        Cuando hago clic en Guardar
        Entonces puedo ver que el usuario "kike2" actualizado en la tabla de usuarios

    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/administracion/usuarios/lista"
        Y inicio sesión con el usuario "juveadmin" y contraseña "123456"
        Y hago clic en Iniciar sesión
        Cuando busque al usuario "angel"
        Entonces puedo ver que el usuario "angel" ya no se encuentra en la tabla de usuarios