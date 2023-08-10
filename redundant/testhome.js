window.onload = displayHomeImage();

function displayHomeImage(){
    var imageString = localStorage.getItem('link-string');
    var img = document.getElementById('image');
    var div = document.getElementById('CC');
    var btn = document.getElementById('button3')
    if (imageString == 'octo/octo-frown.svg') {
        btn.style.background = "crimson";
        div.style.background = "black";
        img.src = imageString;
    }
    else if (imageString == 'octo/octo-smile.svg') {
        btn.style.background = "#120205";
        div.style.background = "crimson";
        img.src = imageString;
    }
}

const msg = localStorage.getItem('message');
const sndr = localStorage.getItem('sender');

document.getElementById('message').textContent = msg;
document.getElementById('sender').textContent = sndr;