
// Datos globales 
interface User {
  username: string,
  latitud: number,
  longitud: number,
  tipoUsuario: string,
  categorias: Array<string>,
}

const etiquetas: HTMLElement = document.getElementById("etiquetas");
var suggestions: Array<string> = [];
var usuarios: Array<User> = [];
var icons: Array<L.Icon> = ["grey", "green", "blue", "violet", "gold"].map((color: string) => {
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
      suggestions = investigadores.map((investigador: User) => {
        return investigador.categorias;
    }).reduce((previous: Array<string>, current: Array<string>) => previous.concat(current),
    []);
    suggestions = Array.from(new Set<string>(suggestions));
    }).then(() => mostrarUsuariosMapa());
}

//Mapa
var markers: Array<L.Marker> = [];
var mapa = L.map('map', {
  center: L.latLng(22.7613421, -102.5828555),
  zoom: 7,
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapa);
var filtros_tipo_usuario: HTMLElement = document.getElementById('filtro_tipo_usuario');

function mostrarUsuariosMapa(): void {
  let filtros: Array<string> = Array.from(filtros_tipo_usuario.children).map((div: HTMLElement) => {
    let input = div.children[0] as HTMLInputElement;
    let label = div.children[1];
    return {
      filtro: label.textContent.trim(),
      activo: input.checked
    };
  }).filter((datos_filtro: { filtro: string, activo: boolean }) => datos_filtro.activo)
    .map((datos_filtro: { filtro: string, activo: boolean }) => datos_filtro.filtro);
  
  let etiquetasRequeridas: Array<string> = Array.from(etiquetas.children).map((etiqueta: HTMLElement) => {
    return etiqueta.textContent.trim();
  });

  let usuarios_filtrados = usuarios.filter((usuario: User) => {
    return filtros.indexOf(usuario.tipoUsuario) != -1;
  });

  usuarios_filtrados.forEach((usuario: User) => {
    let precision: number = usuario.categorias.map((categoria: string) => {
      if(etiquetasRequeridas.indexOf(categoria) != -1) {
        return 1;
      } else {
        return 0;
      }
    }).reduce((previous: number, current: number) => previous + current, 0);
    
    if (precision > 0) {
      precision = Math.floor((icons.length - 1) * (precision / etiquetasRequeridas.length));
      if (precision >= precisionMinima) {
        crearPinMapa(usuario, precision);
      }
    }
  });
}

function limpiarUsuariosMapa(): void {
  markers.forEach((marker: L.Marker) => mapa.removeLayer(marker));
  markers = [];
}

function recargarUsuariosMapa(): void {
  limpiarUsuariosMapa();
  mostrarUsuariosMapa();
}

function crearPinMapa(usuario: User, precision: number): void {
  let m: L.Marker = L.marker([usuario.latitud, usuario.longitud], {icon: icons[precision]});
  m.addTo(mapa).bindPopup(usuario.username);
  markers.push(m);
}

//Sugerencias
const searchWrapper: HTMLElement = document.querySelector(".search-input");
const inputBox: HTMLInputElement = searchWrapper.querySelector("input");
const suggBox: HTMLElement = searchWrapper.querySelector(".autocom-box");

inputBox.onkeyup = (e) => {
  let userData = (e.target as HTMLInputElement).value; //user enetered data
  let emptyArray: Array<string> = [];
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

function select(element: HTMLElement): void {
  let selectData = element.textContent;
  let opt = document.createElement('a');
  opt.className = "btn btn-outline-danger btn-sm etiqueta";
  opt.innerHTML = selectData;
  opt.setAttribute("onclick", "freeSuggestion(this)")
  etiquetas.appendChild(opt);
  suggestions.splice(suggestions.indexOf(selectData), 1);
  inputBox.value = "";
  searchWrapper.classList.remove("active");
  recargarUsuariosMapa();
}

function showSuggestions(list: Array<string>): void {
  let listData: string = list.join('');
  suggBox.innerHTML = listData;
}

function freeSuggestion(opt: HTMLElement): void {
  suggestions.push(opt.textContent.trim());
  opt.remove();
  recargarUsuariosMapa();
}

//Precision
const precisionInput: HTMLInputElement = document.getElementById("precision") as HTMLInputElement;
const precisionBar: HTMLDivElement = document.getElementById("barra-precision") as HTMLDivElement;

function cambiarPrecision(elementoPrecision: HTMLButtonElement): void {
  precisionMinima = +elementoPrecision.value;
  recargarUsuariosMapa();
  actualizarBarraPrecision();
}

function actualizarBarraPrecision(): void {
  let nivelesPrecision: Array<HTMLButtonElement> = Array.from(precisionBar.children).map((nivelPrecision: HTMLElement) => {
    return nivelPrecision as HTMLButtonElement;
  });
  nivelesPrecision.forEach((nivelPrecision: HTMLButtonElement) => {
    nivelPrecision.classList.remove("activo");
  });
  
  for (let i = 0; i < (nivelesPrecision.length - precisionMinima); i++) {
    nivelesPrecision[i].classList.add("activo");
  }
}

obtenerUsuarios();
actualizarBarraPrecision();
