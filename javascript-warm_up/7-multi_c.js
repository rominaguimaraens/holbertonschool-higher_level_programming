#!/usr/bin/node
let counter = 0;

if (parseInt(process.argv[2])) {
  while (process.argv[2] > counter) {
    console.log('C is fun'); counter++;
  }
} else {
  console.log('Missing number of occurrences');
}
