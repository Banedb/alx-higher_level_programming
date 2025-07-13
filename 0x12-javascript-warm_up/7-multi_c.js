#!/usr/bin/node
// Prints `x` times “C is fun” where `x` is the first argument of the script.
if (Number.isFinite(Number(process.argv[2]))) {
  for (let count = parseInt(process.argv[2]); count > 0; count--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
