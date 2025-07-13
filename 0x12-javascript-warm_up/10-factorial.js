#!/usr/bin/node
// Computes and prints a factorial.
function factorial (num) {
  if (num < 0) return -1;
  if (Number.isNaN(num) || num <= 1) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(parseInt(process.argv[2])));
