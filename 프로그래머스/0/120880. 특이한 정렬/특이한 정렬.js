function solution(numlist, n) {
    // 내림차순 정렬
    numlist.sort((a, b) => b - a);
    
    // 차이와 절댓값 계산을 한 번에 처리
    let numlist_index = numlist.map(num => ({ num, diff: Math.abs(num - n) }));
    
    // 차이에 따라 정렬
    numlist_index.sort((a, b) => a.diff - b.diff);
    
    // 정렬된 숫자만 추출
    return numlist_index.map(item => item.num);
}
