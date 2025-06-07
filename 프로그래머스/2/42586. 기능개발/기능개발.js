function solution(progresses, speeds) {
    var answer = [];
    let leftDay = progresses.map((_,i)=> Math.ceil((100-_)/speeds[i]));
    
    let i = 0;
    while(i<progresses.length){
        
        let sucPro = 1; //현재 process는 무조건 배열 안에 들어가니 1
        
        //progresses[i]의 값이 다음값보다 클때 변수에 값 저장
        while(leftDay[i] >= leftDay[i+sucPro]){
            sucPro++;
        }
        
        answer.push(sucPro)
        i+=sucPro //완료된 프로세스 건너뛴 후 인덱스
        
    }
    return answer;
}