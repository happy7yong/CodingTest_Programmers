const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");



function solution(input){
    input = input.map(Number);
    let max = 0;
    let index = 0;
    let answer = [];

    input.forEach((i, idx)=>{

        if(i > max) {
            max = i;
            index = idx+1;

        };

    })

    answer.push(max);
    answer.push(index);

    return answer.join("\n");
}




console.log(solution(input));


