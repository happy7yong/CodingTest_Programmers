function solution(n, arr1, arr2) {
    var newMap = [];
    
    //2진수 변환
    arr1 = arr1.map(num=>num.toString(2)).map(num=>{if(num.length<=n){
            num = "0".repeat(n - num.length)+num
            return num
        }
    })
    arr2 = arr2.map(num=>num.toString(2)).map(num=>{if(num.length<=n){
            num = "0".repeat(n - num.length)+num
            return num
        }
    })
    
    for(let i=0;i<n;i++){
        newMap[i]=[];
        for(let j=0;j<n;j++){
            if(arr1[i][j]==1||arr2[i][j]==1){
                newMap[i].push(1);
            }else{
                newMap[i].push(0);
            }
        }
    }
    //arr1 + arr2 만약 해당 배열에 1이 있을 경우 1 || 이걸 써야할듯
    
    // 1 -> # / 0 -> " "
    for(let i=0;i<n;i++){
        for(let j=0;j<n;j++){
            if(newMap[i][j]==1){
                newMap[i][j]="#";
            }else{
                newMap[i][j]=" ";
            }
        }
        newMap[i] = newMap[i].join("");
    }
    
    return newMap;
}