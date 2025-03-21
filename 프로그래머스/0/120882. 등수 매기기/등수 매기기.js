function solution(score) {
    let score_sum = score.map(num=>num[0]+num[1])
    let score_sort = [...score_sum].sort((a,b)=>b-a)
    return score_sum.map(num=> score_sort.indexOf(num)+1 );
}