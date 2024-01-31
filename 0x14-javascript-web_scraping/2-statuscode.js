#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  }

  // Print the entire response object
  console.log(response);

  // Print only the status code
  console.log(`code: ${response.statusCode}`);
});
