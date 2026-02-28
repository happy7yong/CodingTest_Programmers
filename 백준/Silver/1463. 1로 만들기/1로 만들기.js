//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n) {
  const dp = Array(n + 1).fill(n);

  if (n == 0) return 0;
  if (n == 1) return 0;

  dp[0] = 0;
  dp[1] = dp[0];

  for (let i = 2; i <= n; i++) {
    dp[i] = Math.min(
      i % 2 === 0 ? dp[i / 2] + 1 : n,
      i % 3 === 0 ? dp[i / 3] + 1 : n,
      dp[i - 1] + 1
    );
  }

  return dp[n];
}

const n = Number(input[0]);

console.log(solution(n));

