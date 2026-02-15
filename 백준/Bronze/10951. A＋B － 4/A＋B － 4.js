const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(a,b){
    return a+b;
}

let answer = [];
for(let i =0;i<input.length;i++){
    let [a,b] = input[i].split(" ").map(Number);
    answer.push(solution(a,b));
}

answer = answer.join("\n");
console.log(answer);
