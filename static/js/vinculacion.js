var usuarios = [];
var etiquetas = [];
document.getElementsByClassName("choices")[0].addEventListener('addItem', function (event) { etiquetas.push(event.detail.label); recargarUsuariosMapa(); });
document.getElementsByClassName("choices")[0].addEventListener('removeItem', function (event) { etiquetas.splice(etiquetas.indexOf(event.detail.label), 1); recargarUsuariosMapa(); });
var icons = ["grey", "green", "blue", "violet", "gold"].map((color) => {
    return new L.Icon({
        iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${color}.png`,
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });
});
var precisionMinima = 2;
function obtenerUsuarios(lista_usuarios) {
    usuarios = lista_usuarios;
}
//Mapa
var markers = [];
var mapa = L.map('map', {
    center: L.latLng(22.7613421, -102.5828555),
    zoom: 7,
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapa);
var filtros_tipo_usuario = document.getElementById('filtro_tipo_usuario');
function mostrarUsuariosMapa() {
    let filtros = Array.from(filtros_tipo_usuario.children).map((div) => {
        let input = div.children[0];
        let label = div.children[1];
        return {
            filtro: label.textContent.trim(),
            activo: input.checked
        };
    }).filter((datos_filtro) => datos_filtro.activo)
        .map((datos_filtro) => datos_filtro.filtro);
    let etiquetasRequeridas = etiquetas;
    let usuarios_filtrados = usuarios.filter((usuario) => {
        return filtros.indexOf(usuario.tipoUsuario) != -1;
    });
    usuarios_filtrados.forEach((usuario) => {
        let precision = usuario.categorias.map((categoria) => {
            if (etiquetasRequeridas.indexOf(categoria) != -1) {
                return 1;
            }
            else {
                return 0;
            }
        }).reduce((previous, current) => previous + current, 0);
        if (precision > 0) {
            precision = Math.floor((icons.length - 1) * (precision / etiquetasRequeridas.length));
            if (precision >= precisionMinima) {
                crearPinMapa(usuario, precision);
            }
        }
    });
}
function limpiarUsuariosMapa() {
    markers.forEach((marker) => mapa.removeLayer(marker));
    markers = [];
}
function recargarUsuariosMapa() {
    limpiarUsuariosMapa();
    mostrarUsuariosMapa();
}
function crearPinMapa(usuario, precision) {
    let m = L.marker([usuario.latitud, usuario.longitud], { icon: icons[precision] });
    m.addTo(mapa).bindPopup(`<h3>${usuario.tipoUsuario}: ${usuario.username}</h3><p>Hola</p>`);
    markers.push(m);
}
//Precision
const precisionInput = document.getElementById("precision");
const precisionBar = document.getElementById("barra-precision");
function cambiarPrecision(elementoPrecision) {
    precisionMinima = +elementoPrecision.value;
    recargarUsuariosMapa();
    actualizarBarraPrecision();
}
function actualizarBarraPrecision() {
    let nivelesPrecision = Array.from(precisionBar.children).map((nivelPrecision) => {
        return nivelPrecision;
    });
    nivelesPrecision.forEach((nivelPrecision) => {
        nivelPrecision.classList.remove("activo");
    });
    for (let i = 0; i < (nivelesPrecision.length - precisionMinima); i++) {
        nivelesPrecision[i].classList.add("activo");
    }
}
//Recarga
function reescalarMapa() {
    setTimeout(function () {
        mapa.invalidateSize(true);
    }, 100);
}
actualizarBarraPrecision();
reescalarMapa();
