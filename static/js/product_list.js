
function openfilter(){
    document.querySelector('.filtering').classList.toggle('active');
    document.querySelector('.sorting').classList.remove('active');
}

function opensort(){
    document.querySelector('.sorting').classList.toggle('active');
    document.querySelector('.filtering').classList.remove('active');
}

document.addEventListener('click', function(e){
    if(!e.target.closest('.filters')){
const sorting = document.querySelector('.sorting');
if (sorting) {
    sorting.classList.remove('active');
}
    }
});



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
  });

