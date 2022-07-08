
// Datos globales 
interface User {
  username: string,
  latitud: number,
  longitud: number,
  tipoUsuario: string,
  categorias: Array<string>,
}

interface ChoicesEvent {
  detail: ChoicesDetail,
}

interface ChoicesDetail {
  label: string,
}

var usuarios: Array<User> = [];
var etiquetas: Array<string> = [];
document.getElementsByClassName("choices")[0].addEventListener('addItem', function(event) {etiquetas.push((event as unknown as ChoicesEvent).detail.label); recargarUsuariosMapa()});
document.getElementsByClassName("choices")[0].addEventListener('removeItem', function(event) {etiquetas.splice(etiquetas.indexOf((event as unknown as ChoicesEvent).detail.label), 1); recargarUsuariosMapa()});
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
  let urls: Array<string> = ["investigadores", "empresas", "instituciones_educativas"].map((model: string) => `http://localhost:8000/${model}/fetch`);
  
  Promise.all(urls.map((url: string) => fetch(
    url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    }
  ).then(res => res.json()))).then((usuarios_tipos: Array<Array<User>>) => {
    usuarios_tipos.forEach((usuarios_tipo: Array<User>) => {
      usuarios_tipo.forEach((usuario: User) => {
        usuarios.push(usuario);
      });
    });
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
  
  let etiquetasRequeridas: Array<string> = etiquetas;

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
  m.addTo(mapa).bindPopup(`<h3>${usuario.tipoUsuario}: ${usuario.username}</h3><p>Hola</p>`);
  markers.push(m);
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
//Recarga
function reescalarMapa() {
  setTimeout(function () {
    mapa.invalidateSize(true);
  }, 100);
}

obtenerUsuarios();
actualizarBarraPrecision();
reescalarMapa();
mapa.invalidateSize();
