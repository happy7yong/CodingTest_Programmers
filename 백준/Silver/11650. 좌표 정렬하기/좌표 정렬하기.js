//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, arr) {
  let dots = [];
  for (let a of arr) {
    let [x, y] = a.split(" ").map(Number);
    dots.push({ x: x, y: y });
  }

  dots.sort((a, b) => {
    if (a.x === b.x) return a.y - b.y;
    return a.x - b.x;
  });
  return dots.map((dot) => dot.x + " " + dot.y).join("\n");
}

const n = Number(input[0]);
const arr = input.slice(1);

console.log(solution(n, arr));