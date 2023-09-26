#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
if (!error && response.statusCode == 200) {
    const info = JSON.parse(body);
	console.log(info)
}
});

	
