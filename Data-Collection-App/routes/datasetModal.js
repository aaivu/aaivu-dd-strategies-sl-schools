//Require Mongoose
var mongoose = require('mongoose');

//Define a schema
var Schema = mongoose.Schema;

var DatasetModal = new Schema({
    data :{type : {}},
    date : {type : Date, required : true},
});

module.exports = mongoose.model('Dataset', DatasetModal );