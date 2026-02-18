const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(a, b) {
  return a * b;
}

const [a, b] = input[0].split(" ").map(Number);

console.log(solution(a, b));
