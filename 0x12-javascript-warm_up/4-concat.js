#!/usr/bin/node

const [firstArg, secondArg] = process.argv.slice(2);
console.log(`${firstArg || 'undefined'} is ${secondArg || 'undefined'}`);
