/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return await new Promise(resolve => setTimeout(() => resolve(true), millis));
}


let t = Date.now()
sleep(100).then((result) => console.log(Date.now() - t, result)) // 100