#!/usr/bin/node
const request = require('request');
function countMovies(url) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      const movies = data.results;
      let count = 0;
      for (const movie of movies) {
        if (movie.characters.find(character => character.endsWith('/18/'))) {
          count++;
        }
      }
      if (data.next) {
        countMovies(data.next); // Fetch next page if it exists
      } else {
        console.log(count);
      }
    } else {
      console.log(error);
    }
  });
}
countMovies(process.argv[2]);
