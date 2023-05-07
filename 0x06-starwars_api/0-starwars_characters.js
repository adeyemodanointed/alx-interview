#!/usr/bin/node
const request = require('request');

const val = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${val}`;


request.get(
  "https://swapi-api.alx-tools.com/api/films/3",
  (error, response, body) => {
    if (error) console.log(error);
    const jsonBody = JSON.parse(body);
    const characters = jsonBody.characters;

    const namePerCharacters = characters.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (pError, pResp, pBody) => {
            if (pError) {
              reject(pError);
            }
            resolve(JSON.parse(pBody).name);
          });
        })
    );

    Promise.all(namePerCharacters)
      .then((names) => {
        for (let val in names) {
          console.log(names[val]);
        }
      })
      .catch((err) => console.log(err));
  }
);
