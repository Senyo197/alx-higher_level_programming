#!/usr/bin/node

const [firstArg] = process.argv.slice(2);
const convertedNum = parseInt(firstArg);

function factorial (n) {
  if (n < 0) {
    return -1;
  }
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return (n * factorial(n - 1));
}

console.log(factorial(convertedNum));
