function solution(rank, attendance) {    
    //1. rank에 있는 배열요소 중에 attendance에서 true인 값들 filter
    let rankTrueArr = rank.filter((it, idx)=>attendance[idx]==true);
    let rankSort = rankTrueArr.sort((a,b)=>a-b);
    //let rankAnswer = [];
    
    //randSort의 요소들이 순회하면서 rankTrueArr의 자릿값을 반환한 배열 rankAnswer
    //1. rankSort의 요소의 인덱스를 rank에서 찾기
    //2. 해당 인덱스로 map사용하여 재구성
    let rankAnswer = rankSort.map(it=> rank.indexOf(it));
    return rankAnswer[0]*10000+rankAnswer[1]*100+rankAnswer[2]*1

    
}