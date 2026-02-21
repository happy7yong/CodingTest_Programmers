//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function dfs(start, graph, visited, answer) {
  answer.push(start);
  visited.add(start);

  for (let children of graph[start]) {
    if (!visited.has(children)) {
      dfs(children, graph, visited, answer);
    }
  }
}

function bfs(start, graph, visited, answer) {
  //1. 발자취 남길 큐 생성
  let stepQ = [start];
  visited.add(start);
  answer.push(start);

  //반복할껀데요 빌때까지
  while (stepQ.length) {
    let node = stepQ.shift();

    for (let children of graph[node]) {
      if (!visited.has(children)) {
        visited.add(children);
        stepQ.push(children);
        answer.push(children);
      }
    }
  }
}

function solution(N, M, V, edge) {
  const graph = Array.from({ length: N + 1 }, () => []);

  for (const [u, v] of edge) {
    graph[u].push(v);
    graph[v].push(u);
  }

  for (let i = 0; i <= N; i++) {
    graph[i].sort((a, b) => a - b);
  }

  let dfsAnswer = [];
  let bfsAnswer = [];

  let visited = new Set();
  dfs(V, graph, visited, dfsAnswer);
  visited.clear();
  bfs(V, graph, visited, bfsAnswer);

  return dfsAnswer.join(" ") + "\n" + bfsAnswer.join(" ");
}

const [N, M, V] = input[0].split(" ").map(Number);
const edge = input.splice(1).map((i) => i.split(" ").map(Number));

console.log(solution(N, M, V, edge));
