
//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const N = Number(input[0]);
const paper = input.slice(1).map((i) => i.split(" ").map(Number));

let colorInCount = 0;
let colorOutCount = 0;

function slicePaper(startX, endX, startY, endY, count) {

  let color = paper[startY][startX];

  for (let y = startY; y < endY; y++) {
    for (let x = startX; x < endX; x++) {
      if (paper[y][x] !== color) {
        let midX = Math.floor((startX + endX) / 2);
        let midY = Math.floor((startY + endY) / 2);

        //분할
        //1
        let leftTop = slicePaper(startX, midX, startY, midY, count);
        //2
        let rightTop = slicePaper(midX, endX, startY, midY, count);
        //3
        let leftButtom = slicePaper(startX, midX, midY, endY, count);
        //4
        let rightButtom = slicePaper(midX, endX, midY, endY, count);

        //정복
        return leftTop + rightTop + leftButtom + rightButtom;
      }
    }
  }


  return color === 1 ? colorInCount++ : colorOutCount++;
}

function solution() {
  let count = 0;
  slicePaper(0, N, 0, N, count);

  return [colorOutCount, colorInCount].join("\n");
}

console.log(solution());

