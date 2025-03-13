'use strict';

/**
 * @param {Object} context
 * @param {Array} args
 * @return {null|boolean|number|string|Array|Object}
 */
Function.prototype.callPolyfill = function(context, ...args) {
    return this.call(context, ...args);
}

let fn = function add(b) {
    return this.a + b;
}

let args = [{'a': 5}, 7]
console.log(fn.callPolyfill(...args));