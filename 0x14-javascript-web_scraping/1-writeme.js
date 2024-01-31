#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFileSync(fileName, contentToWrite, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
