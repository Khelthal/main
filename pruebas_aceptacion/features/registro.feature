Característica: Registrarse en el sistema
    Como visitante del sistema
    Quiero regitrar mi cuenta en el sistema
    Para poder utilizar el sistema

    Escenario: Creación de usuario como investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y ingreso el correo "prueba-investigador@prueba.com", el usuario "prueba-investigador" y contraseña "prueba"
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "prueba-investigador" en la página principal

    Escenario: Creación de usuario como empresa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y ingreso el correo "prueba-empresa@prueba.com", el usuario "prueba-empresa" y contraseña "prueba"
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "prueba-empresa" en la página principal

    Escenario: Creación de usuario como institucion educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y ingreso el correo "prueba-institucion@prueba.com", el usuario "prueba-institucion" y contraseña "prueba"
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "prueba-institucion" en la página principal