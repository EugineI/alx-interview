#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchJson (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _, body) => {
      if (err) reject(err);
      else resolve(JSON.parse(body));
    });
  });
}

async function printCharacters () {
  try {
    const film = await fetchJson(apiUrl);
    const characters = film.characters;

    for (const url of characters) {
      const character = await fetchJson(url);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

printCharacters();
