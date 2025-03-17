function solution(lines) {
    var sum = 0;
    var start = [];
    var end = [];
    var am = 0;
    
    //오름차순 포인트 정리
    for(let i=0;i<lines.length;i++){
        start.push(lines[i][0]);
        end.push(lines[i][1]);
    }
    start.sort((a,b)=>a-b)
    end.sort((a,b)=>a-b)                                                                                                                       
    console.log(start,end)
    
    //좌표점
    //0-1 / 1-2 / 0-1 총 3가지 비교
        if(start[1]<=end[0]){
            let am = end[0]-start[1];
        
            start[1]+=am;
            end[0]-=am;
            sum += am;
            
        }
    
        if(start[2]<=end[1]){
            if(start[1]>=start[2]){
                 am = end[1]-start[1]
            }else{
                 am = end[1]-start[2]
            }
            
            
            start[2]+=am;
            end[1]-=am;
            sum+=am;
        }
    
        if(start[2]<=end[0]){
            let am = end[0]-start[2]
            
            start[2]+=am
            end[0]-=am
            sum+=am;
        }
        


    return sum;
}