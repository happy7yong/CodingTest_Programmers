//백준 제출시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, arr, T, P) {
  let pencil = Math.floor(n / P);
  let pencilN = n - P * pencil;

  let count = 0;
  arr.forEach((i) => (count += Math.ceil(i / T)));

  return count + "\n" + `${pencil} ${pencilN}`;
}

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const [T, P] = input[2].split(" ").map(Number);

console.log(solution(n, arr, T, P));