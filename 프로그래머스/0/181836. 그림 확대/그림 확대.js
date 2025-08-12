function solution(picture, k) {
    var answer = [];
    let arr = [2]
    console.log("aa".repeat(2))
    
    picture.map((row)=>
        {
            let rowMap = [...row].map((it)=>it.repeat(k)).join("")
            for(let i=0;i<k;i++){
                answer.push(rowMap)
            }
        }   
    )
    
    return answer
}