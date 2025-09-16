const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const inputNum = Number(input[0]);

function nCr(n,r){
    if(r<0||r>n) return 0n;
    r= Math.min(r,n-r);
    let res = 1n;
    for(let i=1;i<=r;i++){
        let num = BigInt(n-r+i);
        let den = BigInt(i);
        res = (res * num)/den;
    }
    
    return res;
}

for(let i=0; i<inputNum; i++){
    const [wBridge,eBridge] = input[i+1].split(" ").map(Number);
    //총 갯수
    let total = nCr(eBridge, wBridge)

    console.log(total.toString());
}