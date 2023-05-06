#!/usr/bin/node
const request = require('request');

const val = process.argv[2];
console.log(val);
const url = `https://swapi-api.alx-tools.com/api/films/${val}`;

const myPromise = new Promise((resolve, reject) => {
request(url, (error, response, body) => {
  if (error) return;
  const resp = JSON.parse(body).characters;
  const finalResp = [];
  for (let i = 0; i < resp.length; i++) {
new Promise((resolve, reject) => {    
request(resp[i], (error, response, body) => {
console.log(resp[i])
      if (error) return;

      finalResp[i] = (JSON.parse(body).name);
});
}).then(resp => {return})
  }

  resolve(finalResp)
});
})
myPromise.then((resp) => {
console.log(resp)
})

