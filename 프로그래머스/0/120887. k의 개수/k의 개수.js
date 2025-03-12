function solution(i, j, k) {
    var count = 0;
    var k_str = k.toString()
    for(let a=i;a<=j;a++){
        let a_clo= [...a.toString()];
        for(const ele of a_clo){
            if(ele.includes(k_str)){
            
                count++;
            }      
        }
    }
    return count;
}