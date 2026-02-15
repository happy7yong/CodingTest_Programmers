const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");



function solution(n){
    let starStr = "";
    for(let i=1;i<=n;i++){
        for(let j=1;j<=i;j++){
            starStr += "*";
        }
        starStr+="\n";

    }
    return starStr;
}

const n = Number(input[0]);

console.log(solution(n));


