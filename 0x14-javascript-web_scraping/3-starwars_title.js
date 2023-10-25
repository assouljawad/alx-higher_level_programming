#!/usr/bin/node

const id = process.argv[2];
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    const { title } = JSON.parse(body.body);
    console.log(title);
  }
});
