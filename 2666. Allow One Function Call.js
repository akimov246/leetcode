'use strict';

/**
 * @param {Function} fn
 * @return {Function}
 */
let once = function(fn) {

    let wasCalled = false;

    return function(...args){
        if (wasCalled) return undefined;
        wasCalled = true;
        return fn(...args);
    }
};


// let fn = (a,b,c) => (a + b + c)
// let onceFn = once(fn)
//
// console.log(onceFn(1,2,3)); // 6
// console.log(onceFn(2,3,6)); // returns undefined without calling fn
