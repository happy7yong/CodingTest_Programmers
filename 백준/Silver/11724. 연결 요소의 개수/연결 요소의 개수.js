//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function dfs(start, graph, visited) {
  visited.add(start);

  for (const children of graph[start]) {
    if (!visited.has(children)) dfs(children, graph, visited);
  }
}

function solution(N, M, edge) {
  const graph = Array.from({ length: N + 1 }, () => []);
  let visited = new Set();

  //그래프 만들기 : 인접 리스트
  for (const [u, v] of edge) {
    graph[u].push(v);
    graph[v].push(u);
  }

  let count = 0;
  //dfs : 슽택 또는 재귀함수

  for (let i = 1; i <= N; i++) {
    if (!visited.has(i)) {
      count++;
      dfs(i, graph, visited);
    }
  }

  return count;
}

const [N, M] = input[0].split(" ").map(Number);
const edge = input.splice(1).map((i) => i.split(" ").map(Number));

console.log(solution(N, M, edge));
