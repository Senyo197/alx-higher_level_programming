#!/usr/bin/node

const [firstArg] = process.argv.slice(2);
const occurances = parseInt(firstArg);

if (!isNaN(occurances)) {
  for (let i = 0; i < occurances; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
