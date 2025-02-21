function solution(keyinput, board) {
    var answer = [0,0];
    
    xLimit = Math.floor(board[0]/2)
    yLimit = Math.floor(board[1]/2)
    
    
    for(const num of keyinput){
        switch (num){
            case "left" : 
                answer[0] > -xLimit ? answer[0]-=1 : answer[0]+=0;
                break;
            case "right" : 
                answer[0] < xLimit ? answer[0]+=1 : answer[0]+=0;
                break;
            case "up" :
                answer[1] < yLimit ? answer[1]+=1 : answer[1]+=0;
                break;
            case "down" :
                answer[1] > -yLimit ? answer[1]-=1 : answer[1]+=0;
                break;
        }
    }


    
    return answer;
}