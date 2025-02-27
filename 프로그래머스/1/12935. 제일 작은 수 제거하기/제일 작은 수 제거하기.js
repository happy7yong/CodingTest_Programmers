function solution(arr) {
    var answer = [-1];
    var min = Math.min(...arr)
    var arrfilter = arr.filter(num=>min!=num)
    return arr.length > 1 ? arrfilter : answer ;
}