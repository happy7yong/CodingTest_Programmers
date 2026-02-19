//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n) {
  let K5 = 5;
  let K3 = 3;
  let f5 = Math.floor(n / K5);
  let f3 = 0;

  let mK5 = n - K5 * f5; //나머지
  let mK3 = 0;
  let count = 0;

  while (f5 >= 0) {
    if (mK5 % K3 !== 0) {
      f5--;
      mK5 += 5;
    } else if (mK5 % K3 === 0) {
      //0이 되면
      count += f5;
      f3 = mK5 / K3; //K3로 나눴을 때 몫
      mK5 %= K3;
      count += f3;
      break;
    }
  }

  return f5 === -1 ? -1 : count;
}

const n = Number(input[0]);

console.log(solution(n));
