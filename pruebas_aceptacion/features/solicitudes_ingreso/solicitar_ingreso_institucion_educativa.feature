Característica: Solicitar ingreso como institución educativa
    Yo como visitante
    Quiero poder solicitar mi ingreso como institución educativa
    Para poder utilizar todas las funcionalidades de este tipo de usuario

    Escenario: Ningún dato correcto para actualizar a perfil de institucion educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "nombre institucion"

    Escenario: Nombre institución vacía y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "nombre institucion"

    Escenario: Especialidades vacía y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "especialidades"

    Escenario: Miembros vacío y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "miembros"

    Escenario: Código postal vacío y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "codigo postal"

    Escenario: Municipio vacío y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "municipio"

    Escenario: Colonia vacía y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "colonia"

    Escenario: Calle vacía y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "calle"

    Escenario: Númeor exterior vacío y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "numero exterior"

    Escenario: Acerca de vacío y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "acerca de"

    Escenario: Imagen vacía y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "imagen"

    Escenario: Datos de ubicación incorrectos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Apozol" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Villas" en el formulario
        Y relleno el campo de "calle" con "Loles" en el formulario
        Y relleno el campo de "numero exterior" con "12" en el formulario
        Y relleno el campo de "acerca de" con "Somos una institución de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra la notificación de error "Error al obtener los datos de ubicación, por favor verifique que los datos de dirección ingresados son correctos."

    Escenario: Código postal incorrecto y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "9939" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra el mensaje de error "El código postal no tiene un formato válido"

    Escenario: Número exterior incorrecto y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "-1" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me pide que rellene correctamente el campo de "numero exterior"

    Escenario: Imagen incorrecta y los demás correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/incorrecto.txt" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me muestra el mensaje de error "Seleccione una imagen válida. El archivo que ha seleccionado no es una imagen o es un un archivo de imagen corrupto."

    Escenario: Todos los datos correctos para actualizar a perfil de institución educativa
        Dado que ingreso al sistema en el dominio "http://localhost:8000/perfil"
        Y inicio sesión con el usuario "prueba-institucion" y contraseña "prueba"
        Y hago clic en el tipo "Institución Educativa"
        Y relleno el campo de "nombre institucion" con "Institución Juve" en el formulario
        Y elijo "Cloud" en el campo de "especialidades" en el formulario
        Y elijo "prueba-investigador" en el campo de "miembros" en el formulario
        Y relleno el campo de "codigo postal" con "99390" en el formulario
        Y elijo "Jerez" en el campo de "municipio" en el formulario
        Y relleno el campo de "colonia" con "Alamitos" en el formulario
        Y relleno el campo de "calle" con "Mezquite" en el formulario
        Y relleno el campo de "numero exterior" con "29" en el formulario
        Y relleno el campo de "acerca de" con "Soy un institucion de software" en el formulario
        Y relleno el campo de "imagen" con "/tmp/foto.png" en el formulario
        Cuando envío la solicitud presionando el botón de Guardar
        Entonces se me indica que mi solicitud fue enviada