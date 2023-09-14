#!/usr/bin/node
const ls = require('./100-data.js').list;
const List = [];
ls.map((item, i) => {
  return (List[i] = item * i);
});
console.log(ls);
console.log(List);
