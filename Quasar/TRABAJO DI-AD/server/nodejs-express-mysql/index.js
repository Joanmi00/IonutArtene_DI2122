const fs = require('fs');
const https = require('https');
const express = require('express');

const PORT = 5555;

const app = express();

https.createServer({
  key: fs.readFileSync('my_cert.key'),
  cert: fs.readFileSync('my_cert.crt')
}, app).listen(PORT, function () {
  console.log("Servidor HTTPS escoltant al port" + PORT + "...");
});
require("./app/routes/tutorial.routes.js")(app);
app.get("/", (req, res) => {
  res.json({ message: "Welcome to my application." });
});
app.get('/hola', function (req, res) {
  console.log('Hola, em note molt segur.');
});

