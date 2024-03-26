#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

async function getCharacterNames() {
  try {
    const response = await new Promise((resolve, reject) => {
      request.get(url, (error, res, body) => {
        if (error) reject(error);
        resolve(body);
      });
    });

    const data = JSON.parse(response);
    const characterUrls = data.characters;

    for (const characterUrl of characterUrls) {
      const characterResponse = await new Promise((resolve, reject) => {
        request.get(characterUrl, (error, res, body) => {
          if (error) reject(error);
          resolve(body);
        });
      });
      const characterData = JSON.parse(characterResponse);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacterNames();
