Característica: Actualizar cuenta
    Yo como visitante
    Quiero poder actualizar mi cuenta a una cuenta de investigador, empresa o institución educativa
    Para poder utilizar todas las funcionalidades del tipo de cuenta que elija 

    # Ningún dato enviado para perfil de investigador
    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba" y contraseña "prueba"
        Y hago clic en el tipo investigador
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene el campo de "curp"

    # Todos los datos correctos para perfil de investigador
    Escenario: 
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba" y contraseña "prueba"
        Y hago clic en el tipo investigador
        Y relleno el formulario con la CURP: "AUCJ011020HZSGRVA1", el código postal "99390", elijo el municipio "Jerez", la colonia "Alamitos", la calle "Mezquite", el número "29", en acerca de agrego "Soy un investigador de software" y subo la imagen encontrada en "/tmp/foto.png"
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me indica que mi solicitud fue enviada