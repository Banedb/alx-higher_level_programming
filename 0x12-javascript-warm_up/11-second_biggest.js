#!/usr/bin/node
// Searches for the second biggest integer in the list of arguments.
if (process.argv.length <= 3) console.log(0);
else {
  const arr = process.argv.slice(2).map(Number);
  const bigger = arr.sort((a, b) => b - a)[1];
  console.log(bigger);
}
