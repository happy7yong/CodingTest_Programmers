//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(a, b) {
  let MaxG = 0;
  let MinG = 0;
  let count = 0;
  let a_Arr = [];
  let b_Arr = [];

  for (let i = 1; i <= Math.min(a, b); i++) {
    if (a % i == 0 && b % i == 0) {
      MaxG = i;
    }
  }

  //a*b의 최대공약수 찾기
  MinG = (a * b) / MaxG;
  return MaxG + "\n" + MinG;
}

const [a, b] = input[0].split(" ").map(Number);

console.log(solution(a, b));

