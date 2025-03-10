'use strict';

/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
let compactObject = function(obj) {

    function helper(object) {
        let is_arr = Array.isArray(object);
        let result = is_arr ? [] : {};
        for (let key in object) {
            if (object[key]) {
                if (!(object[key] instanceof Object)) {
                    if (is_arr) {
                        result.push(object[key]);
                    } else {
                        result[key] = object[key];
                    }
                } else {
                    if (is_arr) {
                        result.push(helper(object[key]));
                    } else {
                        result[key] = helper(object[key]);
                    }
                }
            }
        }
        return result;
    }

    return helper(obj);
};


let obj = {"a": null, "b": [false, 1]};
obj = [null, 0, 5, [0], [false, 16]];
console.log(compactObject(obj));