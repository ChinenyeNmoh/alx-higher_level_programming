#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
function add (a, b) {
  const result = num1 + num2;
  console.log(result);
}
add(num1, num2);
