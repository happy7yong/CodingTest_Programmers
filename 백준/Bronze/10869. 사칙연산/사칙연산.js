const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(a,b){
    let string = "";
    //A+B, A-B, A*B, A/B(몫), A%B(나머지)
    string += a+b + "\n";
    string += a-b + "\n";
    string += a*b + "\n";
    string += Math.floor(a/b) + "\n";
    string += Math.floor(a%b);

    return string;
}

const [a,b] = input[0].split(" ").map(Number);

console.log(solution(a,b));


