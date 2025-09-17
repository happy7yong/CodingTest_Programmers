const fs = require('fs');
//(/dev/stdin)
const [A,B] = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

let lenDiff = Math.abs(A.length - B.length)
let minDiff = Infinity;

for(let i=0;i<=lenDiff;i++){ //앞에 부분에 차이 나는 만큼 삽입한다고 가정 //사실 뒤에 추가되는거는 생각안해도됨
    //i는 뒤로 한칸씩 미는 역할 완전탐색이 맞긴함.
    let count = 0;
    for(let j=0;j<A.length;j++){
            if(A[j] != B[i+j]) {
                count++;
            }
    }
    minDiff = Math.min(count,minDiff)
}

console.log(minDiff);