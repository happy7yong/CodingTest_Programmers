let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");
let count = Number(input[0]);

let a = [...input[1].trim().split(" ").map(Number)];

for (let i = 0; i < count; i++) {
  if (a[i] >= 300) a[i] = 1;
  else if (a[i] >= 275) a[i] = 2;
  else if (a[i] >= 250) a[i] = 3;
  else a[i] = 4;
}

console.log(a.join(" "));