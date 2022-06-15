const etiquetas = document.getElementById("etiquetas");
var suggestions = ["Software", "Frijol"];
var usuarios = [];
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
function obtenerUsuarios() {
    let url = "http://localhost:8000/investigadores/investigadores";
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json()).catch(error => console.error('Error:', error))
        .then((investigadores) => {
        investigadores.forEach((investigador) => {
            usuarios.push(investigador);
        });
        suggestions = investigadores.map((investigador) => {
            return investigador.categorias;
        }).reduce((previous, current) => previous.concat(current), []);
        suggestions = Array.from(new Set(suggestions));
    }).then(() => mostrarUsuariosMapa());
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
    let etiquetasRequeridas = Array.from(etiquetas.children).map((etiqueta) => {
        return etiqueta.textContent.trim();
    });
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
            console.log(precision);
            crearPinMapa(usuario, precision);
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
    m.addTo(mapa).bindPopup(usuario.username);
    markers.push(m);
}
//Sugerencias
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
inputBox.onkeyup = (e) => {
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if (userData) {
        emptyArray = suggestions.filter((data) => {
            //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data) => {
            // passing return data inside li tag
            return data = `<li>${data}</li>`;
        });
        if (emptyArray.length) {
            searchWrapper.classList.add("active"); //show autocomplete box
            showSuggestions(emptyArray);
        }
        else {
            searchWrapper.classList.remove("active"); //hide autocomplete box
        }
        let allList = suggBox.querySelectorAll("li");
        for (let i = 0; i < allList.length; i++) {
            //adding onclick attribute in all li tag
            allList[i].setAttribute("onclick", "select(this)");
        }
    }
    else {
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
};
function select(element) {
    let selectData = element.textContent;
    let opt = document.createElement('a');
    opt.className = "btn btn-outline-danger btn-sm etiqueta";
    opt.innerHTML = selectData;
    opt.setAttribute("onclick", "freeSuggestion(this)");
    etiquetas.appendChild(opt);
    suggestions.splice(suggestions.indexOf(selectData), 1);
    inputBox.value = "";
    searchWrapper.classList.remove("active");
    recargarUsuariosMapa();
}
function showSuggestions(list) {
    let listData = list.join('');
    suggBox.innerHTML = listData;
}
function freeSuggestion(opt) {
    suggestions.push(opt.textContent.trim());
    opt.remove();
    recargarUsuariosMapa();
}
obtenerUsuarios();