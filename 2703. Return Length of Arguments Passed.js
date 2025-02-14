'use strict';

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
let argumentsLength = function(...args) {
    return arguments.length;
};

console.log(argumentsLength(1, 2, 3)); // 3