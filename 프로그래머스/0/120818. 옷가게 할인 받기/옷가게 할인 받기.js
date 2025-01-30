function solution(price) {
    var answer = price;
    if(500000<=price){
        answer = price*0.8;
    }else if(300000<=price){
        answer = price*0.9
    }else if(100000<=price){
        answer = price*0.95
    }
    return ~~(answer);
}