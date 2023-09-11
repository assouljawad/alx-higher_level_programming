#!/usr/bin/node
const x = process.argv;

function add (a, b) {
  console.log(a + b);
}

add(Number(x[2]), Number(x[3]));
