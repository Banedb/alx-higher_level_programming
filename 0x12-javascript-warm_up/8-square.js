#!/usr/bin/node
// Prints `x` times “C is fun” where `x` is the first argument of the script.
if (Number.isFinite(Number(process.argv[2]))) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
