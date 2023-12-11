#!/usr/bin/node

const [firstArg] = process.argv.slice(2);
const convertNum = parseInt(firstArg);

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertNum}`);
}
