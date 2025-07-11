function solution(n, control) {
    var controlArr = [...control]
    controlArr.forEach((it)=>{
        n += it == "w" ? 1 : it == "s" ? -1 : it == "d" ? 10 : it == "a" ? -10 : 0
    })
    return n;
}