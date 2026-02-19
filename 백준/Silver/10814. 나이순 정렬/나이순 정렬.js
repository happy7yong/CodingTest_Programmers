const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n, arr) {
  //요소 하나는 객체를 의미
  let members = [];

  for (let e of arr) {
    let [age, name] = e.split(" ");
    let member = { age: Number(age), name: name };
    members.push(member);
  }

  //나이순으로 정렬
  members.sort((a, b) => a.age - b.age);

  return members.map((m) => m.age + " " + m.name).join("\n");
}

const n = Number(input[0]);
const arr = input.slice(1);

console.log(solution(n, arr));
