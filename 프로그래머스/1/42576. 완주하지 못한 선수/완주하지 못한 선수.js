function solution(participant, completion) {
    var map = {}; //해쉬
    
    for (let player of participant){
        map[player] = (map[player] || 0) + 1
    }
    
    for(let player of completion){
        map[player]--
    }
    
    for(let player in map){
        if(map[player] > 0) return player;
    }
}