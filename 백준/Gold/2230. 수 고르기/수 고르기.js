const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(M,arr){
    //투포인터
    let leftIndex = 0;
    let rightIndex = 1;
    let min = Infinity;

    arr.sort((a,b)=>a-b);

    let diff = 0;
    //점점 키우는쪽으로 

    while(rightIndex < arr.length){
        diff = arr[rightIndex] - arr[leftIndex];

        if(diff < M){ //아직 작으면
            rightIndex++;
        }else if(diff >= M){
            if(diff < min) min = diff;
            leftIndex++
            if (leftIndex === rightIndex) rightIndex++; // 포인터 겹치면 벌려주기
        }

    }



    return min;

}

const [N, M] = input[0].split(" ").map(Number);
let arr = input.splice(1).map(Number);

console.log(solution(M,arr));

