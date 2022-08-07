// Nav bar
const menu=document.querySelector('.menu');
const close=document.querySelector('.close');
const nav=document.querySelector('nav');

menu.addEventListener('click',function(){
    if (nav.classList.contains('open-nav')){
        nav.classList.remove('open-nav');
    }
    else{
    nav.classList.add('open-nav');
    }
});
