function solution(numbers) {
    var number = {
        "zero" : 0, 
        "one" : 1, 
        "two" : 2, 
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight": 8,
        "nine" : 9
    }
  
    var stack = '';
    var num = '';
    for(let i = 0;i<numbers.length;i++){
        stack += numbers[i];
        if(Object.keys(number).includes(stack)==true){
            num += number[stack]
            stack = ''
        }
    }
    return parseInt(num);
}