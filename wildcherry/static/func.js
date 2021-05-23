$(document).ready(function() {
    $('.slider').slick({
        infinite: true,
        slidesToShow: 1,
        arrows: true,
        dots: true,
        autoplay: true,
        autoplaySpeed: 2000
    });
});

function openbar() {
    document.getElementById('Sidebar').style.width = '25%';
    document.getElementById('shadow').style.zIndex = '5';
    document.getElementById('shadow').style.opacity = '50%';
    var categories = document.querySelectorAll('.category');
    for( let i = 0; i < categories.length; i++){
        categories[i].style.fontSize = '16pt';
    }
}

function closebar() {
    document.getElementById('Sidebar').style.width = '0px';
    document.getElementById('shadow').style.zIndex = '-5';
    document.getElementById('shadow').style.opacity = '0';
    document.getElementById('subcategory').style.zIndex = '-5';
    document.getElementById('subcategory').style.width = '0%';
    var categories = document.querySelectorAll('.category');
    for( let i = 0; i < categories.length; i++){
        categories[i].style.fontSize = '0pt';
    }
}

function open_subcategoies(){
    var category = $(this).attr('id');
    e => span.innerText = category
    document.getElementById('subcategory').style.zIndex = '5';
    document.getElementById('subcategory').style.width = '20%';
    document.getElementById('category').style.fontSize = '16pt';
}


