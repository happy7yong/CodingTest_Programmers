//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n) {
  const dp = Array(n + 1).fill(0);

  if (n == 0) return 0;
  if (n == 1) return 1;
  if (n == 2) return 2;
  if (n == 3) return 4;

  dp[0] = 0;
  dp[1] = 1; // x
  dp[2] = 2; // 1 1
  dp[3] = 4;

  for (let i = 4; i <= n; i++) {
    for (let j = 1; j <= 3; j++) {
      dp[i] += dp[i - j];
    }
  }
  return dp[n];
}

const n = input.slice(1).map(Number);

for (let i of n) {
  console.log(solution(i));
}
