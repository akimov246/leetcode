/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
let chunk = function(arr, size) {
    let chunked_array = [];
    for (let i = 0; i < arr.length; i += size) {
        chunked_array.push(arr.slice(i, i + size));
    }
    return chunked_array;
};

// let arr = [1, 2, 3, 4, 5];
// let size = 1;
// console.log(chunk(arr, size));
//
// arr = [1, 9, 6, 3, 2];
// size = 3;
// console.log(chunk(arr, size));
