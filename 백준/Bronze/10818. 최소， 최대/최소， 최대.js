const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(arr){
    return `${Math.min(...arr)} ${Math.max(...arr)}`;
}

let arr = input[1].split(" ").map(Number);

console.log(solution(arr));
