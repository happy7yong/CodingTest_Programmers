
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const t = Number(input[0]); // 테스트 케이스 수

for (let i = 0; i < t; i++) {
  const n = Number(input[i * 3 + 1]);
  const [x1, y1] = input[i * 3 + 2].split(" ").map(Number);
  const [x2, y2] = input[i * 3 + 3].split(" ").map(Number);

  console.log(solution(n, x1, y1, x2, y2));
}

function solution(n, startX, startY, endX, endY) {
  //1. 탐색할 큐를 생성한다
  const queue = [];

  //방문함을 알리는 visited를 만든다.
  const visited = Array.from({ length: n }, () => Array(n).fill(false));
  //dist를 만든다.
  const dist = Array.from({ length: n }, () => Array(n).fill(0));

  //방향 벡터 만들기
  const dx = [-2, -2, -1, 1, 2, 2, -1, 1];
  const dy = [-1, 1, 2, 2, 1, -1, -2, -2];

  queue.push([startX, startY]);
  visited[startX][startY] = true;

  //큐가 빌때까지 계속 반복
  while (queue.length != 0) {
    let [curX, curY] = queue.shift();

    for (let i = 0; i < 8; i++) {
      let nextX = curX + dx[i];
      let nextY = curY + dy[i];

      if (
        nextX >= 0 &&
        nextX < n &&
        nextY >= 0 &&
        nextY < n &&
        !visited[nextX][nextY]
      ) {
        queue.push([nextX, nextY]);
        visited[nextX][nextY] = true;
        dist[nextX][nextY] = dist[curX][curY] + 1;
      }
    }
  }

  return dist[endX][endY];
}
