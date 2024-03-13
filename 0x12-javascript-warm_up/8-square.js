#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let j = 0; j < parseInt(argv[2]); j++) {
    console.log('X'.repeat(argv[2]));
  }
}
