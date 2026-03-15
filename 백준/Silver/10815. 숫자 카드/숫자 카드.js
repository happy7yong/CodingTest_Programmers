//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, arr) {}

let n = Number(input[0]);
let arr = input[1].split(" ").map(Number);

let m = Number(input[2]);
let arrM = input[3].split(" ").map(Number);
arr.sort((a, b) => a - b);

let answer = [];

for (let i = 0; i < m; i++) {
  answer.push(solution(arrM[i]));
}

//입력값이 크기 때문에 이분탐색인건 확실함
function solution(searchNum) {
  //e : 내가 찾아야하는 값
  let leftIndex = 0;
  let rightIndex = n - 1;

  while (leftIndex <= rightIndex) {
    let midIndex = Math.floor((leftIndex + rightIndex) / 2); //중앙값 target
    // console.log(leftIndex, midIndex, rightIndex);

    if (arr[midIndex] === searchNum) return 1;

    if (arr[midIndex] < searchNum) {
      leftIndex = midIndex + 1;
    } else if (arr[midIndex] > searchNum) {
      rightIndex = midIndex - 1;
    }
  }

  return 0;
}

console.log(answer.join(" "));