//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(K, N, lines) {
  let left = 1;
  let right = Math.max(...lines);
  let answer = left;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    // console.log(mid);
    let totalOfnum = 0;
    for (let line of lines) {
      totalOfnum += Math.floor(line / mid);
    }
    // console.log(totalOfnum);
    if (totalOfnum >= N) {
      answer = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return answer;
}

//이미 갖고 있던 K개
//필요한 랜선 갯수 N개
//목표 : 랜선의 최대 길이  - 모두 동일한 랜선의 길이를 가져야한다.
const [K, N] = input[0].split(" ").map(Number);
const lines = input.slice(1).map(Number);

console.log(solution(K, N, lines));