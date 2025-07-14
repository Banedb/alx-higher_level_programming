#!/usr/bin/node
// Imports a dictionary and inverts the keys and values.
const { dict } = require('./101-data');
const newdict = {};
for (const key in dict) {
  if (!newdict[dict[key]]) newdict[dict[key]] = [];

  newdict[dict[key]].push(key);
}

console.log(newdict);
