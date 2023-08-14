#!/usr/bin/node
const result = process.argv[2];
const convert = parseInt(result);
if (!isNaN(convert)) {
  for (let i = 0; i < convert; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
