#!/usr/bin/node
// Prints "My number: <first argument converted in integer>" if the first
// argument can be converted to an integer else prints "Not a number".
if (Number.isFinite(Number(process.argv[2]))) {
  console.log('My number: ' + parseInt(process.argv[2]));
  // console.log('My number: ' + Math.floor(Number(process.argv[2])));
} else {
  console.log('Not a number');
}
