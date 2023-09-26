#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const object = {};
request(url, (error, res, body) => {
  if (!error && res.statusCode === 200) {
    for (const todo of JSON.parse(body)) {
      if (todo.completed === true) {
        if (object[todo.userId]) {
          object[todo.userId]++;
        } else {
          object[todo.userId] = 1;
        }
      }
    }
  } else {
    console.log(error);
  }
  console.log(object);
});
