//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, arr) {
  const dp = Array(n).fill(0);

  dp[0] = arr[0];
  dp[1] = arr[0] + arr[1];
  dp[2] = Math.max(dp[0] + arr[2], arr[1] + arr[2]);

  for (let i = 3; i < n; i++) {
    dp[i] = Math.max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
  }

  return dp[n - 1];
}

const n = Number(input[0]);
const arr = input.slice(1).map(Number);

console.log(solution(n, arr));
