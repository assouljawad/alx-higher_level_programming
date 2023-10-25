#!/usr/bin/node

const id = process.argv[2];
const request = require('request');
const util = require('util');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const promisReq = util.promisify(request);
request(url, async function (err, body) {
  if (err) {
    console.error(err);
  } else {
    const { characters } = JSON.parse(body.body);
    for (const url of characters) {
      try {
        const { body } = await promisReq(url);
        console.log(JSON.parse(body).name);
      } catch (error) {
        console.error(err);
      }
    }
  }
});
