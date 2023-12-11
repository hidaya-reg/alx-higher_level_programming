#!/usr/bin/node

const { argv } = require('node:process');

const param = parseInt(argv[2]);

if (isNaN(param)) {
  console.log('Not a number');
} else {
  console.log('My number: ', param);
}
