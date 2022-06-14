const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
const etiquetas = document.getElementById("etiquetas");
let linkTag = searchWrapper.querySelector("a");
let webLink;
var suggestions = ["Software", "Frijol"];
var usuarios = [];
var markers = [];
var map = L.map('map', {
    center: L.latLng(22.7613421, -102.5828555),
    zoom: 7,
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
var filtros_tipo_usuario = document.getElementById('filtro_tipo_usuario');
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
    }).then(_ => mostrarUsuariosMapa());
}
function mostrarUsuariosMapa() {
    let filtros = [].slice.call(filtros_tipo_usuario.children).map((div) => {
        let input = div.children[0];
        let label = div.children[1];
        return {
            filtro: label.textContent.trim(),
            activo: input.checked
        };
    }).filter((datos_filtro) => datos_filtro.activo)
        .map((datos_filtro) => datos_filtro.filtro);
    let usuarios_filtrados = usuarios.filter((usuario) => {
        return filtros.indexOf(usuario.tipoUsuario) != -1;
    });
    usuarios_filtrados.forEach(crearPinMapa);
}
function limpiarUsuariosMapa() {
    markers.forEach((marker) => map.removeLayer(marker));
    markers = [];
}
function recargarUsuariosMapa() {
    limpiarUsuariosMapa();
    mostrarUsuariosMapa();
}
function crearPinMapa(usuario) {
    let marker = L.marker([usuario.latitud, usuario.longitud]);
    marker.addTo(map).bindPopup(usuario.username);
    markers.push(marker);
}
inputBox.onkeyup = (e) => {
    let userData = e.target.value; //user enetered data
    let emptyArray = [];
    if (userData) {
        icon.onclick = () => {
            webLink = `https://www.google.com/search?q=${userData}`;
            linkTag.setAttribute("href", webLink);
            linkTag.click();
        };
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
    let opt = document.createElement('option');
    opt.value = selectData;
    opt.innerHTML = selectData;
    let newId = `opcion_${suggestions.length}`;
    opt.setAttribute('id', newId);
    opt.onclick = function () {
        freeSuggestion(event);
    };
    etiquetas.appendChild(opt);
    suggestions.splice(suggestions.indexOf(selectData), 1);
    inputBox.value = "";
    icon.onclick = () => {
        webLink = `https://www.google.com/search?q=${selectData}`;
        linkTag.setAttribute("href", webLink);
        linkTag.click();
    };
    searchWrapper.classList.remove("active");
}
function showSuggestions(list) {
    let listData;
    listData = list.join('');
    suggBox.innerHTML = listData;
}
function freeSuggestion(event) {
    let opt = document.getElementById(event.target.id);
    suggestions.push(opt.value);
    opt.remove();
}
obtenerUsuarios();
