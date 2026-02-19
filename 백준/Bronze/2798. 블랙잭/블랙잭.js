//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, MAX, arr) {
  let arrR = arr.reverse();
  let max = 0;

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      for (let k = j + 1; k < arr.length; k++) {
        sum = arrR[i] + arrR[j] + arrR[k];
        if (sum <= MAX && max < sum) {
          max = sum;
        }
      }
    }
  }
  return max;
}

const [n, MAX] = input[0].split(" ");
const arr = input[1].split(" ").map(Number);

console.log(solution(n, MAX, arr));