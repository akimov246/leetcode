'use strict';

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
let createCounter = function(init) {
    let for_reset = init;
    let count = init;

    return {
        increment: function() {
            return ++count;
        },

        decrement: function() {
            return --count;
        },

        reset: function() {
            return count = for_reset;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */