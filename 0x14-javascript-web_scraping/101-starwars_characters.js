#!/usr/bin/node
const request = require('request');

async function getMovieCharacters(movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
  
  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) reject(error);
        resolve(body);
      });
    });
    
    const movieData = JSON.parse(movieResponse);
    const characters = movieData.characters;
    
    for (const characterUrl of characters) {
      const characterResponse = await new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) reject(error);
          resolve(body);
        });
      });
      
      const characterData = JSON.parse(characterResponse);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error);
  }
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
