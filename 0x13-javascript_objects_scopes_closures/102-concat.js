#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[1];
const fileB = process.argv[2];
const destination = process.argv[3];

const dataA = fs.readFileSync(fileA, 'utf8');
const dataB = fs.readFileSync(fileB, 'utf8');

fs.writeFileSync(destination, dataA + dataB);
