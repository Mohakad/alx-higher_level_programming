#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const se of list) {
    if (searchElement === se) {
      count++;
    }
  }
  return count;
};
