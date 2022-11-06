Característica: Actualizar cuenta
    Yo como visitante
    Quiero poder actualizar mi cuenta a una cuenta de investigador, empresa o institución educativa
    Para poder utilizar todas las funcionalidades del tipo de cuenta que elija 

    # ---------- Actualizar a investigador ---------- #

    Escenario: Ningún dato correcto para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "curp"

    Escenario: CURP vacío y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "curp"

    Escenario: Código postal vacío y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "codigo postal"

    Escenario: Municipio vacío y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "municipio"

    Escenario: Colonia vacía y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "colonia"

    Escenario: Calle vacía y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "calle"

    Escenario: Número exterior vacío y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "numero exterior"

    Escenario: Acerca de vacío y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "acerca de"

    Escenario: Imagen vacía y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "imagen"

    Escenario: CURP incorrecta y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "incorrecto" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra el mensaje de error "El CURP no tiene un formato válido"

    Escenario: Código postal incorrecto y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "9" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra el mensaje de error "El código postal no tiene un formato válido"

    Escenario: Número exterior incorrecto y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "-1" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "numero exterior"

    Escenario: Imagen incorrecta y los demás correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/incorrecto.txt" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra el mensaje de error "Seleccione una imagen válida. El archivo que ha seleccionado no es una imagen o es un un archivo de imagen corrupto."

    Escenario: Datos de ubicación incorrectos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
        Y relleno el campo de "curp" con "AUCJ011020HZSGRVA1" en el formulario
        Y relleno el campo de "codigo postal" con "99394" en el formulario
        Y elijo "Zacatecas" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Durazno" en el formulario
        Y relleno el campo de "calle" con "Juan Aldama" en el formulario
        Y relleno el campo de "numero exterior" con "20" en el formulario
        Y relleno el campo de "acerca de" con "Soy un investigador de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra la notificación de error "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos."

    Escenario: Todos los datos correctos para actualizar a perfil de investigador
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-investigador" y contraseña "prueba"
        Y hago clic en el tipo "Investigador"
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

        # ---------- Actualizar a empresa ---------- #

    Escenario: Ningún dato correcto para actualizar a perfil de empresa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-empresa" y contraseña "prueba"
        Y hago clic en el tipo "Empresa"
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "nombre empresa"