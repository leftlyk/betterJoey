happy = true;
var linkStr = 'octo/octo-smile.svg'; 

function displayImageAngry() {
    linkStr = 'octo/octo-frown.svg';
    localStorage.setItem('link-string', linkStr);
    window.location.href = 'message.html';
   }

function displayImageHappy(){
    linkStr = 'octo/octo-smile.svg';
    localStorage.setItem('link-string', linkStr);
    window.location.href = 'message.html';
}

const form = document.getElementById('form');
const message = document.getElementById('msg');
const sender = document.getElementById('frm');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const messageValue = message.value;
    const senderValue = sender.value;

    localStorage.setItem('message', messageValue);
    localStorage.setItem('sender', senderValue);
})