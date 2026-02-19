//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(a, b) {
  let arr = [];

  for (let i = a; i <= b; i++) {
    arr.push(i);
  }

  let arrSet = new Set([...arr]);

  for (let i of arr) {
    if (i === 1) arrSet.delete(i);
    for (let j = 2; j * j <= i; j++) {
      if (i % j === 0) {
        arrSet.delete(i);
      }
    }
  }

  return [...arrSet].join("\n");
}

const [a, b] = input[0].split(" ").map(Number);

console.log(solution(a, b));