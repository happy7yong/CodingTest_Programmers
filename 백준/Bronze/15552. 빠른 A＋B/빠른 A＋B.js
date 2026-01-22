let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let result = [];
let count = Number(input[0]);
for (let i = 1; i <= count; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  result.push(a + b);
}
console.log(result.join("\n"));

