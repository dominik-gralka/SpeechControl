<html>

<head>
    <title>NeuralTools - SpeechControl Remote</title>
    <link rel="stylesheet" href="css/main.css" type="text/css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap" rel="stylesheet" </head>

<body onload="getQuery()">
    <div class="container">
        <!--<div id="status">
                <div class="circle pulse green"></div>
                 <p id="status-text">Status</p>
                </div>-->
        <div id="box" class="box">

            <div id="left" onclick="requestLeft()">
                <i id="left" class="bi bi-caret-left-fill"></i>
            </div>

            <div id="right" onclick="requestRight()">
                <i id="right" class="bi bi-caret-right-fill"></i>
            </div>

        </div>
    </div>
</body>

<?php
include "request.php";
?>

<script type="text/javascript" src="js/jquery-3.6.0.min.js"></script>
<script src="js/app.js" type="text/javascript"></script>

</html>