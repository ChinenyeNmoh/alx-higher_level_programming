#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  let count = 0;
  for (const i in films) {
    const chars = films[i].characters;
    for (const k in chars) {
      if (chars[k].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
