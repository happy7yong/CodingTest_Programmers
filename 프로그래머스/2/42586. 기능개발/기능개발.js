function solution(progresses, speeds) {
    let returnDay = [];             
    //순서대로 작업이 진행되어야함.
    //day로 시간 조절
    //남은 일수 배열에 남은 일수를 저장하고, 다음 배열의 값이 앞의 프로세스 값보다 작을때, 함께 측정
    
    let leftDay = []; //남은 일수
    
    //progresses남은퍼센트 계산
    for (let p of progresses){
        let leftPro = 100-p;
        leftDay.push(leftPro)
    }
    
    //남은 일수
    for (let i=0;i<speeds.length;i++){
        leftDay[i] = Math.ceil(leftDay[i]/speeds[i])  
    }
    console.log(leftDay);
    let TotalDay = leftDay.length;
    
    for(let curPro=0;curPro<TotalDay;curPro++){
        let NextPro = 1;                                               
        for(NextPro=1;NextPro<=TotalDay-(curPro+1);NextPro++){
            if(leftDay[curPro+NextPro]<=leftDay[curPro]){
                
            }else if(leftDay[curPro+NextPro]>leftDay[curPro]){
                break;
            }
        }
        curPro+=NextPro-1;
        returnDay.push(NextPro);
    }
    
    
    
    
    return returnDay;
}