require('dotenv').config()

// Porta padrão do servidor
const port = process.env.PORT || 3003

const allowCors = require('./cors')
const bodyParser = require('body-parser');
const express = require('express');
const server = express()
const queryParser = require('express-query-int')
const produtosMock = require('../api/produtos/produtosMock');

// CORS


server.use(bodyParser.urlencoded({extended: true}));
server.use(bodyParser.json());
server.use(allowCors)
// Resolver strings que contém em números
server.use(queryParser())

server.listen(port, function () {
    produtosMock.checkDataBase();
    console.log(`BACKEND is running on port ${port}.`);
})

module.exports = server
