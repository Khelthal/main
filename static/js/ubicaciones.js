const filtro_investigadores = document.getElementById('filtro_investigadores');
const filtro_empresas = document.getElementById('filtro_empresas');
const filtro_instituciones = document.getElementById('filtro_instituciones');

var markers=[];

function showUsersInMap() {
  let filtros = [
    {
      filtro : "Investigador",
      checked: filtro_investigadores.checked,
    },
    {
      filtro : "Empresa",
      checked: filtro_empresas.checked,
    },
    {
      filtro : "Institución Educativa",
      checked: filtro_instituciones.checked,
    },
  ];

  let desiredUsers = usuarios.filter(function (usuario) {
    let desired = false;
    filtros.forEach(function (f) {
      if (!f.checked) {
        return;
      }

      if (f.filtro == usuario.tipoUsuario) {
        desired = true;
      }
    });

    return desired;
  });
  desiredUsers.forEach(function (usuario) {
    let marker = L.marker([usuario.latitud, usuario.longitud])
    marker.addTo(map)
      .bindPopup(usuario.tipoUsuario+"  "+usuario.username);
    markers.push(marker);
  });
}

function reloadUsersInMap() {
  cleanUsersInMap();
  showUsersInMap();
}

function cleanUsersInMap() {
  markers.forEach(function (marker) {
    map.removeLayer(marker);
  });
}
