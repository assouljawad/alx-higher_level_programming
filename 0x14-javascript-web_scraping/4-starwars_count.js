#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    let counter = 0;
    const { results } = JSON.parse(body.body);

    results.forEach((element, i) => {
      element.characters.forEach((element, j) => {
        if (element.includes('/18/')) {
          counter++;
        }
      });
    });
    console.log(counter);
  }
});
