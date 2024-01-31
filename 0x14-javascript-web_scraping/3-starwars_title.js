#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const movieData = JSON.parse(body);

  if (movieData.title) {
    console.log(movieData.title);
  }
});
