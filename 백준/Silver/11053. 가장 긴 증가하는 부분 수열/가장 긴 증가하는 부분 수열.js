
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

//가장 긴 수열
//dp

//10 20 10 30 20 50

//dp[i] = i번째 까지의 수열 중 오름차순인 가장 긴 부분 수열의 길이

//dp[0] = 자신을 포함한 1
//dp[1] = 10 20 = 2
//dp[3] = 10 20 10 30 -> 10 20 30 3
//dp[i]

//dp[i] = i번째에서 할수있는것.
//i번째를 사용한다.
//i번째를 사용하지 않는다
const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

function solution(n, arr) {
  const dp = Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (arr[j] < arr[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}

console.log(solution(n, arr));
