function solution(arr) {
    var answer = 0;
    let value = arr;
    let valueBefore = [];
    let count = 0;
    
    while(true){
        value = value.map(num=>{
            if(num>=50 && num%2==0){
                return num/2;
            }else if(num<50 && num%2!=0){
                return num*2+1
            }else{
                return num
            }
        })
        count ++;
        
        if(JSON.stringify(value) == JSON.stringify(valueBefore) || JSON.stringify(value) == JSON.stringify(arr) ){
            break;
        }
        valueBefore = [...value]
    }
    return count-1;
}