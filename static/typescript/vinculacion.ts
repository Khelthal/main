interface User {
  username: string,
  latitud: number,
  longitud: number,
  tipoUsuario: string,
  etiquetas: Array<string>,
}

const searchWrapper: HTMLElement = document.querySelector(".search-input");
const inputBox: HTMLInputElement = searchWrapper.querySelector("input");
const suggBox: HTMLElement = searchWrapper.querySelector(".autocom-box");
const icon: HTMLElement = searchWrapper.querySelector(".icon");
const etiquetas: HTMLElement = document.getElementById("etiquetas");
let linkTag = searchWrapper.querySelector("a");
let webLink;

var suggestions: Array<string> = ["Software", "Frijol"];
var usuarios: Array<User> = [];
var markers: Array<L.Marker> = [];
var map = L.map('map', {
  center: L.latLng(22.7613421, -102.5828555),
  zoom: 7,
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
var filtros_tipo_usuario: HTMLElement = document.getElementById('filtro_tipo_usuario');

function obtenerUsuarios(): void {
  let url: string = "http://localhost:8000/investigadores/investigadores";

  fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(res => res.json()).catch(error => console.error('Error:', error))
    .then((investigadores: Array<User>) => {
      investigadores.forEach((investigador: User) => {
        usuarios.push(investigador);
      });
    }).then(_ => mostrarUsuariosMapa());
}

function mostrarUsuariosMapa(): void {
  let filtros: Array<string> = [].slice.call(filtros_tipo_usuario.children).map((div: HTMLElement) => {
    let input = div.children[0] as HTMLInputElement;
    let label = div.children[1];
    return {
      filtro: label.textContent.trim(),
      activo: input.checked
    };
  }).filter((datos_filtro: { filtro: string, activo: boolean }) => datos_filtro.activo)
    .map((datos_filtro: { filtro: string, activo: boolean }) => datos_filtro.filtro);

  let usuarios_filtrados = usuarios.filter((usuario: User) => {
    return filtros.indexOf(usuario.tipoUsuario) != -1;
  });

  usuarios_filtrados.forEach(crearPinMapa);
}

function limpiarUsuariosMapa(): void {
  markers.forEach((marker: L.Marker) => map.removeLayer(marker));
  markers = [];
}

function recargarUsuariosMapa(): void {
  limpiarUsuariosMapa();
  mostrarUsuariosMapa();
}

function crearPinMapa(usuario: User): void {
  let marker: L.Marker = L.marker([usuario.latitud, usuario.longitud]);
  marker.addTo(map).bindPopup(usuario.username);
  markers.push(marker);
}

inputBox.onkeyup = (e) => {
  let userData = (e.target as HTMLInputElement).value; //user enetered data
  let emptyArray = [];
  if (userData) {
    icon.onclick = () => {
      webLink = `https://www.google.com/search?q=${userData}`;
      linkTag.setAttribute("href", webLink);
      linkTag.click();
    }
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
    } else {
      searchWrapper.classList.remove("active"); //hide autocomplete box
    }
    let allList = suggBox.querySelectorAll("li");
    for (let i = 0; i < allList.length; i++) {
      //adding onclick attribute in all li tag
      allList[i].setAttribute("onclick", "select(this)");
    }
  } else {
    searchWrapper.classList.remove("active"); //hide autocomplete box
  }
}

function select(element) {
  let selectData = element.textContent;
  let opt = document.createElement('option');
  opt.value = selectData;
  opt.innerHTML = selectData;
  let newId = `opcion_${suggestions.length}`;
  opt.setAttribute('id', newId);
  opt.onclick = function() {
    freeSuggestion(event);
  };
  etiquetas.appendChild(opt);
  suggestions.splice(suggestions.indexOf(selectData), 1);
  inputBox.value = "";
  icon.onclick = () => {
    webLink = `https://www.google.com/search?q=${selectData}`;
    linkTag.setAttribute("href", webLink);
    linkTag.click();
  }
  searchWrapper.classList.remove("active");
}

function showSuggestions(list) {
  let listData;
  listData = list.join('');
  suggBox.innerHTML = listData;
}

function freeSuggestion(event) {
  let opt: HTMLOptionElement = document.getElementById(event.target.id) as HTMLOptionElement;
  suggestions.push(opt.value);
  opt.remove();
}

obtenerUsuarios();
