Característica: Registrarse en el sistema
    Como visitante del sistema
    Quiero regitrar mi cuenta en el sistema
    Para poder utilizar el sistema

    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y ingreso el correo "juve@gmail.com", el usuario "juve" y contraseña "123456"
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "juve" en la página principal