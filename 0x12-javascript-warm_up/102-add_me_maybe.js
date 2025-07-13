#!/usr/bin/node
// Increments and calls a function.
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
