#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const request = require('request');

request(args[2], function (err, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(args[3], body.body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
