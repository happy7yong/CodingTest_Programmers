function solution(myStr) {
    var answer = [];
    answer = myStr.split("a")
    let answer1 = answer.map(num=>num.split("b").filter(item=>item.length!==0)).flat()
    let answer2 = answer1.map(num=>num.split("c").filter(item=>item.length!==0)).flat()
    return answer2.length!==0 ? answer2 : ["EMPTY"];
}