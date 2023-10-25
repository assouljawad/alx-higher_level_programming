#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, body) {
  if (err) {
    console.error(err);
  } else {
    const obj = {};
    const data = JSON.parse(body.body);
    data.forEach(element => {
      if (element.completed) {
        const i = element.userId;
        obj[i] ? obj[i] = ++obj[i] : obj[i] = 1;
      }
    });
    console.log(obj);
  }
});
