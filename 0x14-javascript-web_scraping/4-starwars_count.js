#!/usr/bin/node

const req = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

req.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const filmsData = JSON.parse(body);

  const filmsWithWedge = filmsData.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
  );

  console.log(filmsWithWedge.length);
});
