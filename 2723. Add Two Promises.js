/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
let addTwoPromises = async function(promise1, promise2) {
    return await promise1 + await promise2;
};

promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20));
promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60));

addTwoPromises(promise1, promise2)
    .then(result => console.log(result));