Característica: Registrarse en el sistema
    Como visitante del sistema
    Quiero regitrar mi cuenta en el sistema
    Para poder utilizar el sistema

    Escenario: Creación de usuario como investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y relleno el campo de "email" con "prueba-investigador@prueba.com" en el formulario
        Y relleno el campo de "usename" con "prueba-investigador" en el formulario
        Y relleno el campo de "password" con "prueba" en el formulario
        Y relleno el campo de "repassword" con "prueba" en el formulario
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "prueba-investigador" en la página principal

    Escenario: Creación de usuario como empresa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y relleno el campo de "email" con "prueba-empresa@prueba.com" en el formulario
        Y relleno el campo de "usename" con "prueba-empresa" en el formulario
        Y relleno el campo de "password" con "prueba" en el formulario
        Y relleno el campo de "repassword" con "prueba" en el formulario
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "prueba-empresa" en la página principal

    Escenario: Creación de usuario como institucion educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/usuarios/registrar"
        Y relleno el campo de "email" con "prueba-institucion@prueba.com" en el formulario
        Y relleno el campo de "usename" con "prueba-institucion" en el formulario
        Y relleno el campo de "password" con "prueba" en el formulario
        Y relleno el campo de "repassword" con "prueba" en el formulario
        Cuando hago clic en Crear cuenta
        Entonces puedo ver mi nombre de usuario "prueba-institucion" en la página principal