/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
let filter = function(arr, fn) {
    let filtederArr = [];

    arr.forEach((value, index) => {
        if (fn(value, index)) {
            filtederArr.push(value);
        }
    });
    return filtederArr;
};