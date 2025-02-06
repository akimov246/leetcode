/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
let reduce = function(nums, fn, init) {
    let result = init;

    nums.forEach((value) => {
        result = fn(result, value);
    });

    return result;
};