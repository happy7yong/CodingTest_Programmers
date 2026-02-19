//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(n, arr) {
  let MAX = Math.max(...arr);

  let newArr = arr.map((i) => (i / MAX) * 100);

  let sum = newArr.reduce((acc, rec) => acc + rec);

  return sum / n;
}

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

console.log(solution(n, arr));
