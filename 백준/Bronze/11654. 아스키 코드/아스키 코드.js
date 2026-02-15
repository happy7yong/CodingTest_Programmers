
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(a){
    return a.toString().charCodeAt(0);
}


const Asce = input;

console.log(solution(Asce));