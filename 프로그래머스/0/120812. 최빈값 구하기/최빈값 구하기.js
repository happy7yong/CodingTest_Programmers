function solution(array) {
    let max = 0;
    let maxCount = 0;
    let maxKey = 0;
    
    const map = {};
    
    //최빈값 찾기
    //arr의 값을 키로 설정
    for(const arr of array){
        if(map[arr]) {
            map[arr] += 1
        }else{
            map[arr] = 1
        }
    }
    
    
    //가장 값이 큰 키찾기
    for(const m in map){
        max = max < map[m] ? map[m] : max
    }

    
    for(const m in map){
        if(max === map[m]){
            maxCount ++;
            maxKey = m;
        }
    }
    
    return maxCount > 1 ? -1 : parseInt(maxKey);
}