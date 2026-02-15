const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(n){
    let string = "";
    for(let i=1;i<=9;i++){
        string += `${n} * ${i} = ${n*i}`;
        string += "\n";
    }
    
    return string;
    
}

const n = Number(input[0]);

console.log(solution(n));