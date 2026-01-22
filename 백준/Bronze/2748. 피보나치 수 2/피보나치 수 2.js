let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let memo = new Array(n + 1).fill(0n);
memo[0] = 0n;
memo[1] = 1n;
for (let i = 2; i <= n; i++) {
  memo[i] = memo[i - 1] + memo[i - 2];
}

console.log(memo[n].toString());

