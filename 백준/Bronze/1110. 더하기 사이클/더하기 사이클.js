const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const n = Number(input[0]);

function solution() {
  let original = n; // 처음 값 저장
  let answer_arr = n < 10 ? [0, n] : [...n.toString()].map(Number);

  let answer_prev = answer_arr[0];
  let answer_cur = answer_arr[1];

  let answer_new = n;
  let count = 0;

  while (true) {
    let answer_sum = answer_prev + answer_cur;

    // 새로운 숫자 생성
    answer_new = answer_cur * 10 + (answer_sum % 10);

    // 다음 루프를 위한 자리 분리
    answer_prev = Math.floor(answer_new / 10);
    answer_cur = answer_new % 10;

    count++;

    if (answer_new === original) break;
  }

  return count;
}

console.log(solution());
