//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(A, B, V) {
  day = Math.ceil((V - A) / (A - B)) + 1;
  return day;
}

const [A, B, V] = input[0].split(" ").map(Number);

console.log(solution(A, B, V));