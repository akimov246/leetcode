'use strict';

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
let sortBy = function(arr, fn) {
    return arr.toSorted((a, b) => fn(a) - fn(b));
};

// let arr = [5, 4, 1, 2, 3];
// let fn = (x) => x;
// console.log(sortBy(arr, fn));