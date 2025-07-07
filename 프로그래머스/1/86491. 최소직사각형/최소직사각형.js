function solution(sizes) {
    var answer = 0;
    let width = [];
    let height = [];
    //가로의 길이가 더 커야됨.
    //1. 둘의 크기중 더 큰걸 width로 하기
    sizes.forEach((it)=>{
        width.push(Math.max(...it));
        height.push(Math.min(...it));
    })
    let widthMax = Math.max(...width);
    let heightMax = Math.max(...height);
    return widthMax*heightMax;
}