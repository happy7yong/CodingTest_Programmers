function solution(participant, completion) {
    var answer = '';
    let map ={};
    
    for(let people of participant){ //of는 배열 //in map 객체 키순회
        map[people] = (map[people] || 0)+1 
    }
        
    for(let player of completion){
        map[player]--
    }
    
    for(let player in map ){
        if(map[player] > 0)
            return player
    }
    
    return answer;
}