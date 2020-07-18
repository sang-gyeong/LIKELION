const div = document.querySelector('div');
const divs = document.querySelectorAll('div');

const GOLD = '#FFD700';
const BLUE = '#1E90FF';
const WHITE = '#FFFFFF';

div.addEventListener('click', function(event){
    const clicked = event.target;
    const parent = clicked.parentNode;
    divs.forEach(function(d){
        d.style.background = WHITE;
    });
    clicked.style.background = GOLD;
    if (parent.tagName==='DIV'){
        parent.style.background = BLUE;
    }
});
