#!/usr/bin/node

const av = process.argv.sort(function (a, b) {
  return a - b;
});
const len = av.length;

if (len === 2 || len === 3) {
  console.log('0');
} else {
  console.log(av[len - 2]);
}
