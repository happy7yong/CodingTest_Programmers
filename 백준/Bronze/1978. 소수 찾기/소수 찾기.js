//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, arr) {
  let count = 0;
  arr.forEach((e) => {
    if (e === 1) count++;
    for (let i = 2; i * i <= e; i++) {
      if (e % i === 0) {
        //소수가 아닌 것
        count++;
        break;
      }
    }
  });

  return n - count; //전체중 소수가 아닌것을 뺌.
}


const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

console.log(solution(n, arr));