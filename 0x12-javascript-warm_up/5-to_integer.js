#!/usr/bin/node

const param = parseInt(process.argv[2]);

if (isNaN(param) || param === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', param);
}
