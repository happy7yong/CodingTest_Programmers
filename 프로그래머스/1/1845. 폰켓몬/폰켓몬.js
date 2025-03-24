function solution(nums) {
    let map = {} // map 선언
    var count=0;
    
    for(let poketKind of nums){
        map[poketKind] = (map[poketKind] || 0)+1
    }
    for(let key in map){
        count++
        map[key]--
        if(count == nums.length/2)
            break;
    }
    
    
    return count;
}