const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");



function solution(arr){
    arr.sort((a,b) => a-b);
    if(arr[2]*arr[2] == arr[0]*arr[0] + arr[1]*arr[1]) return "right";
    return "wrong";
}

let answer = [];
for(let i=0;i<input.length-1;i++){
    let arr = input[i].split(" ").map(Number);
    answer.push(solution(arr));
}


console.log(answer.join("\n"));