/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (this.at(-1) === undefined) {
        return -1;
    }
    return this.at(-1);
};

// let arr = [null, {}, 3];
// console.log(arr.last());
//
// arr = [];
// console.log(arr.last());