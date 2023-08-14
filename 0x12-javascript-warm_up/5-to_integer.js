#!/usr/bin/node
const result = process.argv[2];
const convert = parseInt(result);
if (!isNaN(convert)) {
  console.log('My number:', convert);
} else {
  console.log('Not a number');
}
