function solution(A, B) {
    var A_arr = [...A]
    var word = [];
    var word_s = "";
    for(let i=0;i<A_arr.length;i++){
        A_arr.map((_,index)=>{
                word[(index+i)%A_arr.length]=_
        })
        
        word_s=word.join("");
        
        if(word_s===B){
            return i
        }
            
    }
    
    return -1

}