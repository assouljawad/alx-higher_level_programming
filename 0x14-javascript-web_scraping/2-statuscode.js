#!/usr/bin/node

const args = process.argv[2];
const request = require('request');

request(args, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
