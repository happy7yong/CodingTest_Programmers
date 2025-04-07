function solution(num_list, n) {
    var answer = [];
    let list = num_list.concat(num_list)
    return list.slice(n,num_list.length+n)
}