function solution(n, lost, reserve) {
    var answer = 0;
    lost.sort((a,b)=>a-b);
    reserve.sort((a,b)=>a-b)
    
    //1. 먼저 reserve와 lost의 번호가 겹치는게 있는지 확인 
    let reserves = reserve.filter(student => !lost.includes(student))
    let losts = lost.filter(student => !reserve.includes(student))
    
    for(let r of reserves){
        let idx = losts.findIndex(l => Math.abs(r-l) === 1) //1단계밖에 차이가 안나는 idx / 잃어버린 학생을 기준으로, 빌려줄수있는 애가 있나확인
        if(idx!=-1)losts.splice(idx,1) // idx에서 1개 삭제
    }
    
    
    
    console.log(losts, reserves)
    
    //못빌린 사람만 빼면됨.
    return n-losts.length;
}