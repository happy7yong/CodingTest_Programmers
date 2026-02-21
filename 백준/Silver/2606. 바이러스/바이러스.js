//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function bfs(start, graph, visited, count) {
  let stepQ = [start];
  visited.add(start);
  let head = 0;

  while (head < stepQ.length) {
    let node = stepQ[head++];

    for (let children of graph[node]) {
      if (!visited.has(children)) {
        visited.add(children);
        stepQ.push(children);
        count++;
      }
    }
  }

  return count;
}

function solution(N, M, edge) {
  const graph = Array.from({ length: N + 1 }, () => []);

  //인접 그래프 만들기
  for (let [u, v] of edge) {
    graph[v].push(u);
    graph[u].push(v);
  }

  let visited = new Set();
  let start = 1;
  let count = 0;

  return bfs(start, graph, visited, count);
}

const [N] = input[0].split(" ").map(Number);
const [M] = input[1].split(" ").map(Number);
const edge = input.splice(2).map((i) => i.split(" ").map(Number));

console.log(solution(N, M, edge));