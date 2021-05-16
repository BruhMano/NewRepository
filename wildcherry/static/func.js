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
}

function closebar() {
    document.getElementById('Sidebar').style.width = '0px';
    document.getElementById('shadow').style.zIndex = '-5';
    document.getElementById('shadow').style.opacity = '0';
}