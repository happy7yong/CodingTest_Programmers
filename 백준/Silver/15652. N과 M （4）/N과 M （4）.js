//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const current = [];
const answer = [];

function dfs(depth) {
  if (depth == M) {
    answer.push([...current]);
    return;
    //여기서 멈춰야됨. 트리거
  }

  for (let i = 1; i <= N; i++) {
    if (current[depth - 1] > i) continue;
    current.push(i);
    dfs(depth + 1);
    current.pop();
  }

  return answer;
}

function solution() {
  return dfs(0)
    .map((i) => i.join(" "))
    .join("\n");
}

console.log(solution());