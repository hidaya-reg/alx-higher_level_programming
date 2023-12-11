#!/usr/bin/node
// Prints message depending on the number of arguments

const args = process.argv.length;

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
