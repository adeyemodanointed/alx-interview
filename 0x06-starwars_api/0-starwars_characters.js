#!/usr/bin/node
const request = require('request');

const val = process.argv[2];
console.log(val);
const url = `https://swapi-api.alx-tools.com/api/films/${val}`;
const finalResp = [];
request(url, (error, response, body) => {
  if (error) return;
  const resp = JSON.parse(body).characters;

  for (let i = 0; i < resp.length; i++) {
    request(resp[i], (error, response, body) => {
      if (error) return;
      finalResp[i] = (JSON.parse(body).name);
    });
  }

  finalResp.forEach(elem => console.log(elem));
});
