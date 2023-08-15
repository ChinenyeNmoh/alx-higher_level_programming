#!/usr/bin/node
const Square01 = require('./5-square');

module.exports = class Square extends Square01 {
  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
    console.log(c.repeat(this.height));
    }
  }
}
