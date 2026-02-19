//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(arr) {
  return arr
    .map(Number)
    .sort((a, b) => a - b)
    .join("\n");
}

const n = Number(input[0]);
const arr = input.slice(1).map(Number);

console.log(solution(arr));