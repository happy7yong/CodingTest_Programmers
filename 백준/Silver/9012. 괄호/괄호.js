//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(arr) {
  let arrSplit = [...arr];
  let stack = [];
  for (let e of arrSplit) {
    if (e === "(") {
      stack.push(e);
    }
    if (e === ")") {
      if (stack.length == 0) return "NO";
      stack.pop(e);
    }
  }
  return stack.length == 0 ? "YES" : "NO";
}

const n = Number(input[0]);
for (let i = 1; i <= n; i++) {
  console.log(solution(input[i]));
}
