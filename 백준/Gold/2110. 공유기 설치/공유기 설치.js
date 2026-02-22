//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

//집 5 공유기 3
//누적합?
//가장 인접한 두 공유기 사이의 거리를 최대로 함.  1 4 9
//M개의 공유기 중 가장 가까운 거리를 최대로 하도록 해야됨. -> 이게 왜 이분탐색임?
//뭐가 정렬이 되어있어야되는거임?

//이자식이 그리드
//placeArr의 갯수 : 200,000개

function placeCheck(placeArr, mid, M) {
  let inPlace = placeArr[0]; //첫집 무조건 설치
  let count = 1;
  //mid는 우리가 놓으려는 정답일까? 하는 것임. 가까운 최솟값
  for (let i = 1; i < placeArr.length; i++) {
    //거리
    let d = placeArr[i] - inPlace;
    if (d >= mid) {
      inPlace = placeArr[i]; //이전 위치 기억
      count++;
    }
  }

  return count >= M;
}

function solution(N, M, placeArr) {
  //비교함수(N log N)
  placeArr.sort((a, b) => a - b);

  //mid는 우리가 구하려는 최소 거리

  let start = 1;
  let end = Math.max(...placeArr);
  while (start <= end) {
    //거리조절
    let mid = Math.floor((start + end) / 2);
    if (placeCheck(placeArr, mid, M)) {
      //설치가능여부 함수
      start = mid + 1;
    } else {
      //가능한 마지막값
      //true(start) true(end) true(그 전에 mid) false false : 이분탐색이라 
      end = mid - 1;
    }
  }
  return end;
}

const [N, M] = input[0].split(" ").map(Number);
const placeArr = input.slice(1).map(Number);

console.log(solution(N, M, placeArr));
