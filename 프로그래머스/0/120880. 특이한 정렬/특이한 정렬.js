function solution(numlist, n) {
    numlist.sort((a,b)=>b-a)
    
    var num_dif = numlist.map(num=>num-n);
    var num_abs = num_dif.map(num=>Math.abs(num))
    var numlist_index = [];
    
    for(let i=0;i<numlist.length;i++){
        let num_min = Math.min(...num_abs)
        numlist_index.push(numlist[num_abs.indexOf(num_min)])
        num_abs[num_abs.indexOf(num_min)]=Infinity
    }

    return numlist_index;
    
}