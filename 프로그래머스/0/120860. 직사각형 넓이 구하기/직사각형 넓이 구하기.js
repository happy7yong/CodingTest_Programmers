function solution(dots) {
    let xMin = Math.min(...dots.map(dot => dot[0]))
    let xMax = Math.max(...dots.map(dot => dot[0]))
    let yMin = Math.min(...dots.map(dot => dot[1]))
    let yMax = Math.max(...dots.map(dot => dot[1]))
    return (xMax-xMin)*(yMax-yMin);
}