function solution(score) {
    var answer = [];
    //평균 점수
    let score_age = score.map(s=>(s[0]+s[1])/2)
    let score_sort = [...score_age].sort((a,b)=>b-a);
    return score_age.map(_=>score_sort.indexOf(_)+1);
}