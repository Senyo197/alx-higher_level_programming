#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

function secondBiggestNum (array) {
  if (array.length < 2) {
    return 0;
  }

  const sortedArgs = array.sort((a, b) => b - a);
  return sortedArgs[1];
}

console.log(secondBiggestNum(args));
