function solution(numbers, n) {
    var sum = 0;
    numbers.some(num=>{
        sum += num
        return sum > n //some 메서드를 통해 조건에 해당할 경우 return 으로 for문 나감.
    })
    return sum;
}