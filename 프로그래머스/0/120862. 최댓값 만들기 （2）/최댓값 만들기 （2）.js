function solution(numbers) {
    var num = numbers.sort((a,b)=>b-a);
    var a_b = num[num.length-1]*num[num.length-2];
    var b_a = num[0]*num[1]
    var sum = 0;
    a_b > b_a ? sum = a_b : sum = b_a
    return sum;
}