#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const [firstArg, secondArg] = process.argv.slice(2);

const num1 = parseInt(firstArg);
const num2 = parseInt(secondArg);

if (!isNaN(firstArg) && !isNaN(secondArg)) {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}
