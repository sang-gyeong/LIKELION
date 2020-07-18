const parent = document.querySelector('.parent');
const son = document.querySelector('#son');
const daughter = parent.querySelector('#daughter');

son.classList.add('red');
daughter.classList.add('big');
//html마크업을 손대지않고 자바스크립트에서 건드릴 수 있는 것!

const children = document.querySelectorAll('.child2');
console.log(children);

children.forEach(child2 => {
    child2.classList.add('gold');
});

console.log('textContent : ' + son.textContent);
console.log('innerText : ' + son.innerText);
console.log('innerHTML : ' + son.innerHTML);

const father = document.createElement('p');
father.textContent = '저도 자식입니다.';

parent.appendChild(father);

father.setAttribute('id', 'father');
father.setAttribute('class', 'parent');

console.log(father);