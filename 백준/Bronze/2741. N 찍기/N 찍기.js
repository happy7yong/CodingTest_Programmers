//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(num) {
  let answer = [];
  for (let i = 1; i <= num; i++) {
    answer.push(i);
  }
  return answer.join("\n");
}

const num = Number(input[0]);

console.log(solution(num));