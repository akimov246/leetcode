/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
let cancellable = function(fn, args, t) {
    let start = Date.now();
    console.log(fn.call(this, ...args), Date.now() - start);
    let timerID = setInterval(() => console.log(fn.call(this, ...args), Date.now() - start), t);
    return function () {
        clearInterval(timerID);
    }
};

const cancelTimeMs = 190;
const cancelFn = cancellable((x) => x * 2, [4], 35);
setTimeout(cancelFn, cancelTimeMs);