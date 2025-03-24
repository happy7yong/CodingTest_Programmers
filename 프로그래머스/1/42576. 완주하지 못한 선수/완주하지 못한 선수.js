function solution(participant, completion) {
    var map = {};
    
    //0. 해쉬맵 초기화
    for(let player of participant){
        map[player]=0
    }
    
    //1. 해쉬맵에 저장
    for(let player of participant){
        map[player]+=1
    }
    //2. 해쉬맵에서 제거
    for(let player of completion){
        map[player]--
    }
    //3. 남아있는 사람
    for(let player in map){
        if(map[player]>0)
            return player
    }
}