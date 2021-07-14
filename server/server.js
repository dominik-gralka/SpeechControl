// Require express and body-parser
const express = require("express")
const bodyParser = require("body-parser")
const { json } = require("body-parser")
var fs = require('fs');
var https = require('https')

// Initialize express and define a port
const app = express()
const PORT = 3000

// Tell express to use body-parser's JSON parsing
app.use(bodyParser.json())

app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', '*');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', '*');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    //res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
}, bodyParser.json());



app.post('/webhook', (req, res) => {

    console.log('--------------------------------------\n\n Incoming API Request\n api.constellate.de\n')
    console.log(req.body)

    var apiSecret = (req.body).apiSecret;

    var data = (req.body).data;

    var object = req.body;
    object = JSON.stringify(object);

    if (apiSecret == null) {
        res.status(403).end()
        console.log('\x1b[35m%s\x1b[0m', '\n Request incomplete - Cancelled \n');
        console.log('--------------------------------------\n')
        return;
    }
    else {
        res.status(200).end()
    }
    
    if (data == "terminate") {
        // Terminates request named after apiSecret
        fs.unlinkSync('sessions/' + apiSecret + '.json', function (err) {
            if (err) throw err;
        }); 
        /*fs.writeFile('sessions/' + apiSecret + '.json', object, function(err, result) {
            if(err) console.log('error', err);
        });*/
        console.log('\x1b[35m%s\x1b[0m', '\n Request termination (' + apiSecret + '.json' + ') successfully initiated.\n');
        console.log('--------------------------------------\n')
    }
    else {
        // Creates file named after apiSecret
        fs.writeFile('sessions/' + apiSecret + '.json', object, function(err, result) {
            if(err) console.log('error', err);
        });
        console.log('\x1b[35m%s\x1b[0m', '\n Request (' + apiSecret + '.json' + ') successfully queued.\n');      
        console.log('--------------------------------------\n')
    }


  })

// Start express on the defined port
app.listen(PORT, () => (
    console.log('--------------------------------------\n'),
    console.log(' Constellate API'),
    console.log(' api.constellate.de\n'),
    console.log('\x1b[36m%s\x1b[0m', ` Server running on port ${PORT}\n`),
    console.log('--------------------------------------\n')
))
