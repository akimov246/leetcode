'use strict';

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
let promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let results = [];
        let counter = 0;

        functions.forEach((f, i) => {
            f()
                .then(result => {
                    results[i] = result;
                    counter++;
                    if (counter === functions.length) {
                        resolve(results);
                    }
                })
                .catch(error => {
                    reject(error);
                });
        });
    });
};


// const promise = promiseAll([
//     () => new Promise(resolve => setTimeout(() => resolve(4), 50)),
//     () => new Promise(resolve => setTimeout(() => resolve(10), 200)),
//     () => new Promise(resolve => setTimeout(() => resolve(16), 100))
// ]);
// promise.then(console.log); // [42]
