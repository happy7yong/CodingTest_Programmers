//백준 제출 시
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const n = input[0].split("").map(Number);

n.sort((a, b) => b - a);

console.log(n.join(""));