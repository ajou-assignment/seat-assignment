Array.prototype.division = function (denominator) {
    let arr = this;
    let len = arr.length;
    let count =
        Math.floor(len / denominator) +
        (Math.floor(len % denominator) > 0 ? 1 : 0);
    let result = [];

    for (let i = 0; i < count; i++) {
        result.push(arr.splice(0, denominator));
    }

    return result;
};
