//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, money, kindOfmoney) {

  let count = 0;

  for (let i = n - 1; i >= 0; i--) {
    let currentCount = 0;
    if (money >= kindOfmoney[i]) {
      currentCount = Math.floor(money / kindOfmoney[i]);
      count += currentCount;
      money -= kindOfmoney[i] * currentCount;
    }
  }

  return count;
}

const [n, money] = input[0].split(" ").map(Number);
const kindOfmoney = input.slice(1);

console.log(solution(n, money, kindOfmoney));