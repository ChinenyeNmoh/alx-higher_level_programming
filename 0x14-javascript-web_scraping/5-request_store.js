#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(filename, body, (error) => {
    if (error) console.log(error);
  });
});
