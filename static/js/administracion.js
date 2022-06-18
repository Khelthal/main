const sideBarMenu = document.getElementById('sidebar-menu-container');
function marcarMenuActivo(menu) {
    Array.from(sideBarMenu.children).forEach((child) => {
        if (child.children[0].textContent.trim().toLocaleLowerCase() == menu.toLocaleLowerCase()) {
            child.classList.add("active");
        }
    });
}
