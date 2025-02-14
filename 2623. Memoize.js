'use strict';

/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {

    let cache = new Map();

    return function(...args) {
        if (cache.has(args.toString())) return cache.get(args.toString());

        let result = fn(...args);
        cache.set(args.toString(), result);
        return result;
    }
}

// let sum = (a, b) => a + b;
//
// const memoizedSum = memoize(sum);
//
// console.log(memoizedSum(2, 2));
// console.log(memoizedSum(2, 2));
// console.log(memoizedSum(1, 2));