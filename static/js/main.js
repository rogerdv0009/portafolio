/*Hacer que la barra de progreso se actualice con el scroll*/
let docElem = document.documentElement;
let progress = document.getElementById('progress');

window.addEventListener('scroll', () => {
    let winScroll = window.scrollY;
    let height = docElem.scrollHeight - docElem.clientHeight;
    let scrolled = (winScroll / height) * 100;
    progress.style.width = scrolled + "%";
});

/*########################################################################*/
