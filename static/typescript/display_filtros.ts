const searchMenu: HTMLElement = document.getElementById('search-side');
const filtroBtnOut: HTMLElement = document.getElementById('filtro-btn-out');


function hideSearchSide(): void {
    searchMenu.classList.add("hide-element");
    filtroBtnOut.classList.remove("hide-element");
}

function showSearchSide(): void {
    searchMenu.classList.remove("hide-element");
    filtroBtnOut.classList.add("hide-element");
}
