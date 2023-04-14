const width = 180;    // We will scale the photo width to this
const height = 0;     // This will be computed based on the input stream
const streaming = false;
let video = null;
let canvas = null;
let photo = null;
let startbutton = null;

function startup() {
    try {
        video = document.getElementById('video');
        canvas = document.getElementById('canvas');
        photo = document.getElementById('photo');
        startbutton = document.getElementById('startbutton');

        navigator.mediaDevices
            .getUserMedia({ video: true, audio: false })
            .then((stream) => {
                video.srcObject = stream;
                video.play();
            })
            .catch((err) => {
                console.error(`An error occurred: ${err}`);
            });
    }
    catch (e) {
        alert(navigator.mediaDevices)
    }
}

document.addEventListener('DOMContentLoaded', startup)