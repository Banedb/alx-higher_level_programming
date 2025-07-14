#!/usr/bin/node
// Imports an array and computes a new array.
const { list } = require('./100-data');
const newlist = list.map((item, idx) => item * idx);
console.log(list);
console.log(newlist);
