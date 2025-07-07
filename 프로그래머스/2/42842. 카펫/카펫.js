function solution(brown, yellow) {
    var answer = [];
    const total = brown + yellow
    let width = 0;
    let height = 0;
    //brown은 테두리 
    //테두리=brown의 특징 
    //가로*2+세로*2-4 =
    //가로 세로 조건 1. total의 값이 나와야됨.즉 약수값중있음 2. 가로*2+세로*2-4=
    for(let i=1;i<=total;i++){
        if(total%i==0){//약수
            if((i*2+(total/i*2)-4)==brown){
                height = i
                width = total/i
                break;
            }
        }
    }
    return [width, height];
}