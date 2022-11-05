Característica: Actualizar cuenta
    Yo como visitante
    Quiero poder actualizar mi cuenta a una cuenta de investigador, empresa o institución educativa
    Para poder utilizar todas las funcionalidades del tipo de cuenta que elija 

    # Ningún dato enviado para perfil de investigador
    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo investigador
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene el campo de "curp"

    # Todos los datos correctos para perfil de investigador
    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo investigador
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me indica que mi solicitud fue enviada