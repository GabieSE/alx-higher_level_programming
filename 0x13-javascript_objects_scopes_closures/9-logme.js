#!/usr/bin/node
let ptr = 0;
exports.logMe = function (item) {
  console.log(`${ptr++}: ${item}`);
};
