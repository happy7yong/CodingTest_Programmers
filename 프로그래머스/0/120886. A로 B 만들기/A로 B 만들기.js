const Counter = (Spell) => {
    var Spell_arr = [...Spell];
    var Spell_set = [...new Set(Spell_arr)]
    
    var Counter_arr = Spell_set.map(num=>({
        speill : num,
        count : Spell_arr.filter(before_item=>before_item==num).length
    }))
    
    return Counter_arr
}

function solution(before, after) {
    
    let count_before = Counter(before)
    let count_after = Counter(after)
    
    console.log(count_before, count_after)
    var answer = count_before.map(num=>count_after.map((item=>num.speill==item.speill && num.count==item.count? 1:0)))
    var count_answer = answer.map(num=>num.filter(item=>item==1).length==0?0:1)

    return count_answer.length == count_answer.filter(num=>num==1).length?1:0;
}