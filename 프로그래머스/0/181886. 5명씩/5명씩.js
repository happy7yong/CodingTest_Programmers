function solution(names) {
    var answer = [];
    return names.filter((num,index)=>index%5==0 ? num : 0);
}