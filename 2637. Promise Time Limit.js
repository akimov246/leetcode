/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
let timeLimit = function(fn, t) {

    return async function(...args) {
        return await Promise.race([
            fn.call(this, ...args),
            new Promise((resolve, reject) => setTimeout(() => reject('Time Limit Exceeded'), t))
        ])
    }
};

let fn = async (n) => {
    await new Promise(res => setTimeout(res, 100));
    return n * n;
};

fn = timeLimit(fn, 50);
(async () => {
    try {
        console.log(await fn([5]));
    } catch (err) {
        console.error(err);
    }
})();