function solution(id_pw, db) {
    let order = [-1,-1];
    let answer = ''
    
    //프로퍼티를 각각 비교 
    for(let i=0;i<db.length;i++){
        if(id_pw[0] == db[i][0]){
            order[0] = i
        }
        
        if(id_pw[1] == db[i][1]){
            order[1] = i
        }
    }

    //order 중 string 찾기 / 숫자 null로 만들기 
    console.log(order)
    if(order[0] == order[1]){
        answer = "login"
    }else if(order[0] == -1){
        answer = "fail"
    }else{
        answer = "wrong pw"
    }

    return answer;
}