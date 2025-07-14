#!/usr/bin/node
// Defines a square and inherits from `Square` of `5-square.js`.
const BaseSquare = require('./5-square');
module.exports = class Square extends BaseSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
