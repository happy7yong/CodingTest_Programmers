const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(value){
    let v = [...value].map(Number);
    return v.reduce((arr,cur) => arr+cur);

}


const value = input[1];

console.log(solution(value));