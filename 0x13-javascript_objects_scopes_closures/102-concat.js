#!/usr/bin/node
// Concats 2 files into a third file.
const fs = require('fs');
if (process.argv.length === 5) {
  fs.writeFileSync(process.argv[4], fs.readFileSync(process.argv[2], 'utf8') +
                   fs.readFileSync(process.argv[3], 'utf8'));
}
