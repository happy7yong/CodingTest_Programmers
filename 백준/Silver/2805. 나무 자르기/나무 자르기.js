//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(N, M, trees) {
  let left = 0;
  let right = Math.max(...trees);
  let answer = left;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    // console.log(mid);
    let total = 0;
    for (let tree of trees) {
      let value = tree - mid;
      total += value > 0 ? value : 0;
    }
    // console.log(total);

    if (total >= M) {
      answer = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return answer;
}

//N:나무 갯수
//M:가져갈 길이
const [N, M] = input[0].split(" ").map(Number);
const trees = input[1].split(" ").map(Number);

console.log(solution(N, M, trees));
