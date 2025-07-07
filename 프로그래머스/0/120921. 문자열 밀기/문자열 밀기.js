function solution(A, B) {
    
    
    for(let i=0;i<A.length;i++){
        const shiftA = A.slice(A.length-i) + A.slice(0,A.length-i)
        console.log(shiftA)
        if(shiftA === B){
            return i
        }
    }
    return -1;
}