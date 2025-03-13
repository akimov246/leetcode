'use strict';

class ArrayWrapper {
    constructor(nums) {
        this.nums = nums;
        this.sum = this.nums.reduce((acc, num) => acc + num, 0);
    }

    valueOf() {
        return this.sum;
    }

    toString() {
        return `[${this.nums.join(',')}]`
    }
}

// const obj1 = new ArrayWrapper([1, 2]);
// const obj2 = new ArrayWrapper([3, 4]);
// console.log(String(obj1));
// console.log(String(obj2));
// console.log(obj1 + obj2);

