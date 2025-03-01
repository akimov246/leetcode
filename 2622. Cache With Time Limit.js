'use strict';

class TimeLimitedCache {

    constructor() {
        this.cache = new Map();
    }

    set(key, value, duration) {
        let val, dur;
        if (this.cache.has(key)) {
            [val, dur] = this.cache.get(key);
        }
        let result = Boolean((val || val === 0) && dur >= Date.now());
        this.cache.set(key, [value, Date.now() + duration]);
        return result
    }

    get(key) {
        let val, dur;
        if (this.cache.has(key)) {
            [val, dur] = this.cache.get(key);
        }
        return ((val || val === 0) && dur >= Date.now()) ? val : -1;
    }

    count() {
        let counter = 0;

        this.cache.forEach((value, key) => {
            let [, dur] = value;
            if (dur >= Date.now()) {
                counter++;
            }
        });

        return counter;
    }
}

let test = new TimeLimitedCache();
console.log(test.set(1, 42, 100));
console.log(test.get(1));
console.log(test.count());