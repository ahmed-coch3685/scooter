
// const track = document.querySelector(".slider-track");

// const cards = document.querySelectorAll(".product-card");

// const nextBtn = document.querySelector(".next-btn");

// const prevBtn = document.querySelector(".prev-btn");

// let index = 0;

// let cardsPerView = 3;

// function updateCardsPerView() {

//     if (window.innerWidth <= 768)
//         cardsPerView = 1;
//     else
//         cardsPerView = 3;
// }

// updateCardsPerView();

// window.addEventListener("resize", updateCardsPerView);

// function moveSlider() {

//     const cardWidth = cards[0].offsetWidth;

//     track.style.transform =
//         `translateX(-${index * cardWidth}px)`;
// }

// nextBtn.addEventListener("click", () => {

//     if (index < cards.length - cardsPerView) {

//         index++;

//     } else {

//         index = 0;

//     }

//     moveSlider();
// });

// prevBtn.addEventListener("click", () => {

//     if (index > 0) {

//         index--;

//     } else {

//         index = cards.length - cardsPerView;

//     }

//     moveSlider();
// });


// /* auto slide */

// setInterval(() => {

//     if (index < cards.length - cardsPerView) {

//         index++;

//     } else {

//         index = 0;

//     }

//     moveSlider();

// }, 3000);

document.addEventListener("DOMContentLoaded", function () {

    function initFlickity(selector, options) {
        var element = document.querySelector(selector);

        if (element) {
            return new Flickity(element, options);
        }
    }

    const defaultOptions = {
        cellAlign: 'center',
        wrapAround: true,
        autoPlay: 4000,
        prevNextButtons: true,
        pageDots: true,
        draggable: true,
        contain: true
    };

    initFlickity('.featured-carousel', defaultOptions);
    initFlickity('.cat-carousel', defaultOptions);
    initFlickity('.offer-carousel', defaultOptions);
    initFlickity('.new-carousel', defaultOptions);

    initFlickity('.banner-carousel', {
        cellAlign: 'center',
        wrapAround: true,
        autoPlay: 5000,
        prevNextButtons: false,
        pageDots: true,
        draggable: true,
        adaptiveHeight: true
    });

    initFlickity('.dete-carousel', {
        cellAlign: 'left',
        wrapAround: true,
        autoPlay: 5000,
        prevNextButtons: false,
        pageDots: true,
        draggable: true,
        adaptiveHeight: true
    });

});