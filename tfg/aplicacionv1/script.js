var video = document.querySelector("#videoElement");
var captureBtn = document.querySelector("#captureBtn");
var canvas = document.createElement("canvas");
var context = canvas.getContext("2d");

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
        })
        .catch(function(error) {
            console.log("Error al acceder a la cámara: " + error);
        });
} else {
    console.log("El navegador no es compatible con la captura de video.");
}

function captureImage() {
    var originalWidth = canvas.width;
    var originalHeight = canvas.height;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    var imageData = canvas.toDataURL("image/jpeg", 1);

    canvas.width = originalWidth;
    canvas.height = originalHeight;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "guardar_imagen.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("Imagen guardada exitosamente.");
        }
    };
    xhr.send("imageData=" + encodeURIComponent(imageData));
}

document.getElementById("captureBtn").addEventListener("click", function() {
    captureImage();
});

document.getElementById("nuevaPartidaBtn").addEventListener("click", function() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "nueva_partida.php", true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("Comandos ejecutados exitosamente.");
        }
    };
    xhr.send();
});


document.getElementById("reconocerPosicionBtn").addEventListener("click", function() {
    var originalWidth = canvas.width;
    var originalHeight = canvas.height;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    var imageData = canvas.toDataURL("image/jpeg", 1);

    canvas.width = originalWidth;
    canvas.height = originalHeight;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "reconocer_posicion.php", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {

        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("Imagen guardada exitosamente.");
        }
    };
    xhr.send("imageData=" + encodeURIComponent(imageData));
});

