function solution(arr, intervals) {
    var answer = [];
    let slice1 = arr.slice(intervals[0][0],intervals[0][1]+1)
    let slice2 = arr.slice(intervals[1][0],intervals[1][1]+1)
    return slice1.concat(slice2);
}