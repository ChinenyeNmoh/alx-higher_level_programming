#!/usr/bin/node
const result = process.argv.slice(2);
if (result.length <= 1) {
  console.log('0');
} else{
  convertedarray = [];
for (let i = 0; i < result.length; i++) {
  const convertednums = +result[i];
  convertedarray.push(convertednums);
}
convertedarray.sort((a, b) => b - a);
console.log(convertedarray[1]);
}
