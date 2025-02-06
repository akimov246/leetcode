/**
 * @param {Function[]} functions
 * @return {Function}
 */
let compose = function(functions) {
    let clone = functions.toReversed();

    return function(x) {
        return clone.reduce((accum, fn) => fn(accum), x);
    }
};


const fn = compose([x => x + 1, x => 2 * x]);
console.log(fn(4));