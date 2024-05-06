<?php
session_start();
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aplicación v1</title>
    <link rel="stylesheet" type="text/css" href="assets/chessground.base.css">
    <link rel="stylesheet" type="text/css" href="assets/chessground.brown.css">
    <link rel="stylesheet" type="text/css" href="assets/chessground.cburnett.css">
    <style>
        #chessground {
            width: 500px;
            height: 500px;
        }

        cg-board {
            background-color: #bfcfdd;
        }

        #videoContainer {
            width: 640px;
            height: 480px;
            background-color: #666;
            overflow: hidden;
        }
        #videoElement {
            width: 640px;
            height: 480px;
        }
    </style>
    
    <script type="module">
    import { Chessground } from './node_modules/chessground/chessground.js';

    const config = {
        highlight: {
            lastMove: true,
            check: false
        },
        viewOnly: false
    };

    const ground = Chessground(document.getElementById('chessground'), config);

    function updateBoardWithFEN(fen) {
        config.fen = fen;
        ground.set(config);
    }

    function fetchAndUpdateFEN() {
	fetch('/tfg/aplicacionv1/FEN.txt')
    		.then(response => response.text())
    		.then(fen => {
        updateBoardWithFEN(fen);
    })
    .catch(error => console.error('Error fetching FEN:', error));

    }

    setInterval(fetchAndUpdateFEN, 1000);
</script>

</head>
<body>
    <h1>Aplicación v1</h1>
    <div id="videoContainer">
        <video id="videoElement" controls autoplay></video>
    </div>
    <canvas id="canvas" style="display: none;"></canvas>
    <button id="nuevaPartidaBtn">Nueva partida</button>
    <button id="captureBtn">Hacer captura</button>
    <button id="reconocerPosicionBtn">Reconocer posición</button>
    <script src="script.js"></script>
    
    <div id="chessground"></div>

</body>
</html>
