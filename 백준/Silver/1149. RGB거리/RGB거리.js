//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const n = Number(input[0]);
const colorArr = input.slice(1).map((i) => i.split(" ").map(Number));

function solution() {
  const dp = Array.from({ length: n }, () => Array(3).fill(0));
  

  //작은 문제로 큰문제를 푼다.
  dp[0][0] = colorArr[0][0];
  dp[0][1] = colorArr[0][1];
  dp[0][2] = colorArr[0][2];

  for (let i = 1; i < n; i++) {
    dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + colorArr[i][0];
    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + colorArr[i][1];
    dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + colorArr[i][2];
  }

  return Math.min(...dp[n - 1]);
}

console.log(solution());
