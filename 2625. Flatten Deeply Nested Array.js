/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
let flat = function (arr, n) {

    function helper(arr, n) {
        while (n) {
            let current_arr = [];
            let inner_arrays_counter = 0;
            arr.forEach((item) => {
                if (Object.prototype.toString.call(item) === '[object Array]') {
                    current_arr.push(...item);
                    inner_arrays_counter++;
                } else {
                    current_arr.push(item);
                }
            });
            arr = current_arr;
            if (inner_arrays_counter) {
                n--;
            } else {
                n = 0;
            }
        }
        return arr;
    }

    return helper(arr, n);
};

let arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]];
let n = 1;
console.log(flat(arr, n));
console.log(arr);