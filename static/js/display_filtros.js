const searchMenu = document.getElementById('search-side');
const filtroBtnOut = document.getElementById('filtro-btn-out');
function hideSearchSide() {
    searchMenu.classList.add("hide-element");
    filtroBtnOut.classList.remove("hide-element");
}
function showSearchSide() {
    searchMenu.classList.remove("hide-element");
    filtroBtnOut.classList.add("hide-element");
}
