function solution(intStrs, k, s, l) {
    let answer = [];
    intStrs.map(num=>
        num.slice(s,s+l)>k?answer.push(parseInt(num.slice(s,s+l))):0
    )

    return answer;
}