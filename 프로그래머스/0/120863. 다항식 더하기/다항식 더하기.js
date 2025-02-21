function solution(polynomial) {
    var stack = 0;
    var poly = [...polynomial];
    
    //다항식 차수
    for(let i=0;i<poly.length;i++){
        if(poly[i]=="x"){
            isNaN(parseInt(poly[i-1])) ? stack+=1  : 
            isNaN(parseInt(poly[i-2])) ? stack += parseInt(poly[i-1]) : stack += parseInt(poly[i-2]+poly[i-1]);
        }
    }
    var order = stack==1 ? "x": stack+"x"
    
    //다항식 상수
    var poly_num = polynomial.split(" ").map(Number).filter((num)=>isNaN(num)==false);
    
    //답
    var answer = poly_num.length==0 ? 
        order : stack==0
            ? poly_num.reduce((acc,cur)=>acc+cur) : 
                order+" + "+poly_num.reduce((acc,cur)=>acc+cur)
    
    return answer.toString();
}