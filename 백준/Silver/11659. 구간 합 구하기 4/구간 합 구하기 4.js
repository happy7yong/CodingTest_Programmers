//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(N, M, arr, point) {
  let answer = [];
  let prefixArr = Array.from({ length: N + 1 }).fill(0);

  //누접합 배열을 미리 만들어 두기
  //0 5 9 14 ...
  for (let i = 1; i <= N; i++) {
    prefixArr[i] = prefixArr[i - 1] + arr[i - 1];
  }

  for (let [i, j] of point) {
    let sum = 0;
    sum = prefixArr[j] - prefixArr[i - 1];
    answer.push(sum);
  }
  return answer.join("\n");
}

const [N, M] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);
const point = input.splice(2).map((i) => i.split(" ").map(Number));

console.log(solution(N, M, arr, point));