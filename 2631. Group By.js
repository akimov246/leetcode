/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let grouped = {};
    this.forEach((value) => {
        let result = fn.call(this, value);
        if (Object.hasOwn(grouped, result)) {
            grouped[result].push(value);
        } else {
            grouped[result] = [value];
        }
    });

    return grouped;
};

// let array = [
//     {'id': '1'},
//     {'id': '1'},
//     {'id': '2'},
// ];
//
// let fn = function(item) {
//     return item.id;
// };
//
// console.log(array.groupBy(fn));