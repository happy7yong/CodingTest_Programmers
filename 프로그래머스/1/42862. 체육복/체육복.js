function solution(n, lost, reserve) {
    var answer = 0;
    lost.sort((a,b)=>a-b);
    reserve.sort((a,b)=>a-b);
    
    //앞이나 뒤만 빌려줄수있음. => 값이 하나밖에 차이나지 않는 학생들의 번호만 서로 빌려줄수있음.
    //reserve가 있지만 lost한 학생들은 결국 하나밖에없음. => 중복학생들은 지움
    let losts = lost.filter(_=>!reserve.includes(_));
    let reserves = reserve.filter(_=>!lost.includes(_));
    
    for(let r of reserves){
        let idx = losts.findIndex(i=>Math.abs(i-r)==1)
        if (idx!=-1)losts.splice(idx, 1)//자르기를 splice()
    }
    
    console.log(losts,reserves);
    return n-losts.length;
}