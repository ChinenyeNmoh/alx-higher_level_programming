#!/usr/bin/node
const result = process.argv[2];
const convert = parseInt(result);
if (!isNaN(convert)) {
  for (let i = 0; i < convert; i++) {
    console.log('X'.repeat(convert));
  }
} else {
  console.log('Missing size');
}
