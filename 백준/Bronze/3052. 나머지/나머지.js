//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const arr = input.slice(0).map(Number);
const answer = [];
for (let i of arr) {
  answer.push(i % 42);
}

let dup = new Set(answer);

console.log(dup.size);