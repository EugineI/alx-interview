#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(filmUrl, (err, res, body) => {
  if (err) return;

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach((url) => {
    request(url, (err2, res2, body2) => {
      if (!err2) {
        const character = JSON.parse(body2);
        console.log(character.name);
      }
    });
  });
});
