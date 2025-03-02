/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
let join = function(arr1, arr2) {
    let arr = {};
    [...arr1, ...arr2].forEach((obj) => {
        if (obj.id in arr) {
            arr[obj.id].push(obj);
        } else {
            arr[obj.id] = [obj];
        }
    });

    let joinedArr = [];
    //console.log(arr);
    for (let id in arr) {
        joinedArr.push({...arr[id][0], ...arr[id][1]});
    }

    return joinedArr.toSorted((a, b) => a.id - b.id);
};

let arr1 = [{"id": 1,"x": 2,"y": 3},{"id": 2,"x": 3,"y": 6}];
let arr2 = [{"id": 2,"x": 10,"y": 20},{"id": 3,"x": 0,"y": 0}];

console.log(join(arr1, arr2));