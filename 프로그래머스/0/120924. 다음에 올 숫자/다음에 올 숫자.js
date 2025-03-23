function solution(common) {
    var answer = 0;
    let d = common[1]-common[0]
    
    if(common[1]+d==common[2]){
        answer = common[common.length-1]+d //등차확인
    }else{
        let r = common[1]/common[0]
        answer = common[common.length-1]*r
    }
    return answer;
}