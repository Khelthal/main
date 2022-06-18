const sideBarMenu: HTMLElement = document.getElementById('sidebar-menu-container');

function marcarMenuActivo(menu: string): void {
  Array.from(sideBarMenu.children).forEach((child: HTMLElement) => {
    if (child.children[0].textContent.trim().toLocaleLowerCase() == menu.toLocaleLowerCase()) {
      child.classList.add("active");
    }
  });
}
