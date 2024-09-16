
/***Hacer que el switch de cambio de tema dark o ligth cambie***/
const swith = document.getElementById("switch");
document.addEventListener("DOMContentLoaded", () => {
    LoadLightModeInLocalStorage();
    swith.addEventListener("click", LightMode);
})

function LightMode() {
    swith.classList.toggle("ligth_mode");
    document.body.classList.toggle("ligth_mode");
    SaveLightModeInLocalStorage(swith.classList.contains("ligth_mode"));
}

function SaveLightModeInLocalStorage(state) {
    localStorage.setItem("ligth_mode", state);
}

function LoadLightModeInLocalStorage() {
    let light_mode_saved = localStorage.getItem("ligth_mode") === "true";
    if (light_mode_saved) {
        swith.classList.add("ligth_mode");
        document.body.classList.add("ligth_mode");
    }
}
/*#####################################################################*/

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

/*Hacer que funcionar el swipper de Proyectos*/

var swiper = new Swiper(".mySwiperProjects", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        576: {
            slidesPerView: 2,
        },
        992: {
            slidesPerView: 3,
        },
    },
});

/*########################################################################*/