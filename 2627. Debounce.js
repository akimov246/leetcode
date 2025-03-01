'use strict';

/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
let debounce = function(fn, t) {

    let executed = false;
    let timeoutID;

    return function(...args) {
        if (executed) {
            clearTimeout(timeoutID);
            timeoutID = setTimeout(() => {
                fn.call(this, ...args);
                executed = false
            }, t);
        } else {
            executed = true;
            timeoutID = setTimeout(() => {
                fn.call(this, ...args);
                executed = false;
            }, t);
        }
    }
};

// let start = Date.now();
// let f = () => {console.log(Date.now() - start)};
// f = debounce(f, 35);
// setTimeout(f, 30);
// setTimeout(f, 60);
// setTimeout(f, 100);
