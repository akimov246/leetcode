'use strict';

class EventEmitter {

    constructor() {
        this.events = {};
    }
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        if (eventName in this.events) {
            this.events[eventName].push(callback);
        } else {
            this.events[eventName] = [callback];
        }

        return {
            unsubscribe: () => {
                let index = this.events[eventName].indexOf(callback);
                if (~index) {
                    this.events[eventName].splice(index, 1);
                }
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let result = [];
        if (eventName in this.events) {
            for (let callback of this.events[eventName]) {
                result.push(callback.call(this, ...args));
            }
        }
        return result;
    }
}

const emitter = new EventEmitter();
const sub1 = emitter.subscribe('firstEvent', x => x + 1);
const sub2 = emitter.subscribe('firstEvent', x => x + 2);
sub1.unsubscribe();
emitter.emit('firstEvent', [5]);