var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var ds = require("./datasetModal");

router.post('/create', function(req, res, next) {
    ds.create({
        data: req.body,
        date: new Date()
    }, function (err, result) {
        res.jsonp({success:true, id: result._id});
    })
});

router.post('/:id/update', function(req, res, next) {
    ds.findById(req.params.id, function (err, data) {
        data.data[req.query.page] = req.body;
        data.markModified('data');
        data.save(function (err2, result) {
            res.jsonp({success:true});
        })
    });
});

router.get('/:id', function (req, res) {
   ds.findById(req.params.id, function (err, data) {
       res.jsonp({err: err, data:data});
   })
});

router.get('/:id/:page', function (req, res) {
    ds.findById(req.params.id, function (err, data) {
        res.jsonp({err: err, page: data.data[req.params.page]});
    })
});


module.exports = router;
