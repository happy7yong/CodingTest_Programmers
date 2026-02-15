const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(n, string){
    let answer = "";

    answer = [...string].map(i=>i.repeat(n)).join("");

    console.log(answer);

    return answer;
}


const n = Number(input[0]);

let answer = [];
for(let i =1;i<input.length;i++){
    let [n, string] = input[i].split(" ");
    answer.push(solution(n, string));
}

answer.join("\n");