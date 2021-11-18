Array.prototype.division = function (denominator) {
    let arr = this;
    let len = arr.length;
    let result = [];

    for (let i = 0; i < denominator; i++) {
        result.push(arr.splice(0, len / denominator));
    }
    if (arr) {
        for (let i = 0; i < arr.length; i++) {
            result[i].push(arr[i]);
        }
    }

    return result;
};

/*Array.prototype.division = function (denominator) {
    let arr = this;
    let len = arr.length;
    let count =
        Math.floor(len / denominator) +
        (Math.floor(len % denominator) > 0 ? len % denominator : 0);
    let result = [];

    for (let i = 0; i <= count; i++) {
        result.push(arr.splice(0, len / denominator));
    }
    if (arr) {
        for (let i = 0; i < arr.length; i++) {
            result[i].push(arr[i]);
        }
    }

    return result;
};*/
