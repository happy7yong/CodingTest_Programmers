function solution(arr, delete_list) {
    var answer = [];
    return arr.filter(num=>!delete_list.includes(num));
}