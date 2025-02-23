function solution(spell, dic) {
    var spell_arr = dic.map((num)=>spell.map((ind)=>num.includes(ind)))
    var count = new Array(spell_arr.length).fill(0);
    var answer = 2;
    
    spell_arr.forEach((row,index)=>{
        row.forEach((ele)=>{
            if(ele==true){
                count[index]+=1
            }  
        });
       if(row.length==count[index]) {
           answer = 1;
       }
    });
    return answer
    
}