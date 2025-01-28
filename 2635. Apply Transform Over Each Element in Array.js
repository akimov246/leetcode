/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
let map = function(arr, fn) {
    let result = [];

    arr.forEach((value, index) => {
        result.push(fn(value, index));
    })

    return result;
};