function solution(common) {
    var answer = 0;
    let r = common[1]-common[0]
    if(common[1]+r==common[2]){
        answer = common[common.length-1]+r //등비확인
    }else{
        r = common[1]/common[0]
        answer = common[common.length-1]*r
    }
    return answer;
}