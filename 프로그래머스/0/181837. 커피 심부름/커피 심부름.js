function solution(order) {
    var answer = 0;
    let amer = ["iceamericano", "americanoice"	,"hotamericano", "americanohot","americano","anything"]
    let cafe = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot","cafelatte"]
    
    answer = order.map(coffee=>
        amer.some(am=>am==coffee) ? 4500 : cafe.some(ca=>ca==coffee) ? 5000 : 0
    )
    
    return answer.reduce((c,a)=>c+a);
}