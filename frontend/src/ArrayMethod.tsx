export const division = (targetArray:Array<any>, denominator:number):Array<any> => {
    let len = targetArray.length;
    let result = [];

    for (let i = 0; i < denominator; i++) {
        result.push(targetArray.splice(0, len / denominator));
    }
    if (targetArray) {
        for (let i = 0; i < targetArray.length; i++) {
            result[i].push(targetArray[i]);
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
