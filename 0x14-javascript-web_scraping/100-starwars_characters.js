#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    const { characters } = JSON.parse(body.body);
    characters.forEach(url => {
      request(url, function (err, body) {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body.body).name);
        }
      });
    });
  }
});
