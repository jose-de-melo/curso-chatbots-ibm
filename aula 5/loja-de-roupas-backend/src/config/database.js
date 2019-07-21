require('dotenv').config()

const mongoose = require('mongoose');
mongoose.Promise = global.Promise

const uriMongo = process.env.MONGODB_URI || 'mongodb://localhost/loja-de-roupas'

module.exports = mongoose.connect(uriMongo, {useNewUrlParser: true});

