function solution(my_string) {
    return [...my_string].map((num) => num.toLowerCase()).sort().join("");
}