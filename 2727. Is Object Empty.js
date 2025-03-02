/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
let isEmpty = function(obj) {
    return Boolean(!Object.keys(obj).length);
};

// let obj = {"x": 5, "y": 42};
// console.log(isEmpty(obj));
//
// obj = {};
// console.log(isEmpty(obj));
//
// obj = [null, false, 0];
// console.log(isEmpty(obj));