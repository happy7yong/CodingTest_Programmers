function solution(array) {
    return [...array.join("")].map(Number).filter((n) =>  n==7).length;
}