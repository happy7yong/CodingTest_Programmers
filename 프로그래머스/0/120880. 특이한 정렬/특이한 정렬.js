function solution(numlist, n) {
    numlist.sort((a,b)=>b-a)
    
    let numlist_diff = numlist.map(num=>({
        num:num,
        diff:Math.abs(num-n)
    }))
    
    numlist_diff.sort((a,b)=>a.diff-b.diff)
    return numlist_diff.map(item=>item.num)
}
