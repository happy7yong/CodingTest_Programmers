function solution(myString) {
    var answer = '';
    let ismall = ['a','b','c','d','e','f','g','h','i','j','k'];
    
    let StringArr = [...myString].map(i=>ismall.includes(i)?"l":i)
    return StringArr.join("");
}