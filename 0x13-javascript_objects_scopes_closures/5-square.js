#!/usr/bin/node
/* create a class square which inherits from rectangle */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
