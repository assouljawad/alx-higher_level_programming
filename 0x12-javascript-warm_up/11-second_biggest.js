#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length <= 1) {
  console.log('0');
} else {
  const list = argv;
  list.sort().reverse();
  console.log(list[1]);
}
