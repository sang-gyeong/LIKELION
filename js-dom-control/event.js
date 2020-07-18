const title = document.querySelector('.title');
const buttons = document.querySelectorAll('.button');

const WHITE = '#ffffff';
const GRAY = '#f2f2f2';

// title.addEventListener('mouseover', function(event){
//     event.target.style.color = WHITE;
//     console.log(event);
// });

// title.addEventListener('mouseout', function(event){
//     event.target.style.color = GRAY;
//     console.log(event);
// });


// title.addEventListener('click', function(event){
//     event.target.textContent = '배고파요';
//     console.log(event);
// });

// button.addEventListener('click', function(event){
//     title.textContent = '배고파요';
//     console.log(event);
// });


buttons.forEach(function(button){
    button.addEventListener('click', function(event){
        event.target.textContent = '짜잔';
        console.log(event.target);
    });
});

const result= document.querySelector('#result');
const input = document.querySelector('#input');

input.addEventListener('keyup', function(event){
    let pressedKey = '';
    pressedKey = event.key;

    if (pressedKey === 'Enter' ||
    pressedKey === 'Alt'||
    pressedKey === 'Control'||
    pressedKey === 'Shift'){
        result.textContent = pressedKey + '키를 눌렀네요!';
    }
});

window.addEventListener('offline', () => {
	console.log('와이파이 꺼졌어요');
});

window.addEventListener('online', () => {
	console.log('와이파이 켜졌어요');
});


