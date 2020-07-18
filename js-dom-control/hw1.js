const input = document.querySelector('.input');
const all = document.querySelector('.all');
const word_only = document.querySelector('.word_only');


input.addEventListener('keyup', function(e){
    let redex = /\s/ig; //공백, 줄바꿈
    let word = event.target.value;
    let trimed = word.replace(redex, "");
  
    all.textContent = word.length;
    word_only.textContent = trimed.length;
});

