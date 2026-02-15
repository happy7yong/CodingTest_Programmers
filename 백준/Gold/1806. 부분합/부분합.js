const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(n,arr){
    let minScope = Infinity;
    let leftIndex = 0;
    let rightIndex = 0;
    let currentSum = 0;


    while(rightIndex < arr.length){
        currentSum += arr[rightIndex];

        while(currentSum >= n){
            let currentScope = rightIndex - leftIndex+1;
            if(minScope > currentScope) minScope = currentScope;

            currentSum -= arr[leftIndex];
            leftIndex++;
        }

        rightIndex++;

    }


     return minScope == Infinity ? 0 : minScope;

}

const n = Number(input[0].split(" ")[1]);
let arr = input[1].split(" ").map(Number);

console.log(solution(n,arr));
