function solution(clothes) {
    let clothMap = {} //map추가 
    
    //2차원 배열에서 요소별로 hashmap으로 입력받기
    for(let cloth of clothes){
        let clothKind = cloth[1]
        let clothName = cloth[0]
        if(!clothMap[clothKind]){
            clothMap[clothKind] = []
        }
        clothMap[clothKind].push(clothName)
    }
    
    let clothCount = 1
    //각 map에 있는 요소 갯수를 구하기
    for(let [key, value] of Object.entries(clothMap)){
        clothCount *= (value.length+1)
    }

    
    
    return clothCount-1;
}