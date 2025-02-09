document.addEventListener('DOMContentLoaded', function () {

  const sidebar = document.getElementById('sidebar');
  const closeBtn = document.getElementById('sidebar__close-btn');
  const openBtn = document.getElementById('navbar__menu-icon');

  function openSidebar() {
    sidebar.style.width = "400px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }

  function closeSidebar() {
    sidebar.style.width = "0";
    document.body.style.backgroundColor = "white";
  }

  openBtn.addEventListener('click', openSidebar);
  closeBtn.addEventListener('click', closeSidebar);

  document.addEventListener('click', function (event) {
    if (!sidebar.contains(event.target) && !openBtn.contains(event.target) && !closeBtn.contains(event.target)) {
      closeSidebar();
    }
  });

});
