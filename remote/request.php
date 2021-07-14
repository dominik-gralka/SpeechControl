<?php

$query = $_SERVER['QUERY_STRING'];

if ($query == 'q=left') {
    executeLeft();
    return;
}
else if ($query == 'q=right'){
    executeRight();
    return;
}

function execute($data) {
    $url = "https://constellate-api.ultrahook.com/";

    $apiSecret = $_SERVER['REQUEST_URI'];
    $apiSecret = preg_replace("/[^A-Za-z0-9 ]/", '', $apiSecret);

    $headers = [ 'Content-Type: application/json; charset=utf-8' ];
    $POST = [ 'data' => $data, 'apiSecret' => $apiSecret];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($POST));
    $response   = curl_exec($ch);
}

function executeRight() {
    execute('right');
}

function executeLeft() {
    execute('left');
}

?>