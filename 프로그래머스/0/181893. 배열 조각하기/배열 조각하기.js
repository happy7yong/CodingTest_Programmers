function solution(arr, query) {
    query.forEach((v,i)=>{

        if(i%2===0){ //짝수

            arr.splice(v+1);

        }else if(i%2!==0){ //홀수

            arr.splice(0,v);

        }
    })
    return arr;
}