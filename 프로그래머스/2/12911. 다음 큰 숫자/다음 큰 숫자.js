function solution(n) {
    var answer = 0;
    let numOfOne = n.toString(2).split("").filter(i=>i=="1").length;
    let numOfTwo = 0;
    
    do{
        n++;
        numOfTwo = n.toString(2).split("").filter(i=>i=="1").length;
    }while(numOfOne != numOfTwo) //1의 갯수가 같아질때까지 n++
    answer = n
    
    return answer;
}