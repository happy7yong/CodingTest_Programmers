function solution(s) {
    console.log(Number(s))
    return /^\d{4}$|^\d{6}$/.test(s);
}