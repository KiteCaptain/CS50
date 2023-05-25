function greet() 
{
    let name = document.querySelector("#name").value;
    alert("hello, " + name); 
}

document.querySelector("form").addEventListener('submit', greet);

document.addEventListener('DOMContentLoaded', () => {
    let input = document.querySelector('input');
    input.addEventListener('keyup', (event)=> {
        let name = document.querySelector('.greetings');
        if (input.value) {
            name.innerHTML = `Hello, ${input.value}!`;
        }
        else {
            name.innerHTML = "Hello, Guest!"
        }
    })
})

let nav = document.querySelector(".nav")
document.querySelector('#R').onclick = () => {
nav.style.backgroundColor = 'red'
}
document.querySelector('#G').onclick = () => {
    nav.style.backgroundColor = 'green'
}
document.querySelector('#B').onclick = () => {
    nav.style.backgroundColor = 'blue'
}

locationElement = document.querySelector('#current-location')
navigator.geolocation.getCurrentPosition(function(position){
    locationElement.innerHTML = position.coords.latitude + ", " + position.coords.longitude 
})