const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(n,arr){
    arr.sort((a,b)=>{
        if(a.length == b.length){
            return a.localeCompare(b);
        }

        return a.length - b.length;
    });


    return arr;

}

// 길이가 짧은 것부터
// 길이가 같으면 사전 순으로
// 단, 중복된 단어는 하나만 남기고 제거해야 한다.

const n = Number(input[0]);
let arr = input.slice(1);
arr = [...new Set(arr)]

console.log(solution(n, arr).join("\n"));
