function solution(array) {
    var counter = {};
    
    // 배열의 요소를 세는 부분
    for (var i = 0; i < array.length; i++) {
        var arr = array[i];
        
        if (counter[arr]) {
            counter[arr] += 1;
        } else {
            counter[arr] = 1;
        }
    }
    
    var maxCount = 0;
    var maxElements = [];

    // 최빈값을 찾는 부분
    for (var key in counter) {
        if (counter[key] > maxCount) {
            maxCount = counter[key];
            maxElements = [key]; // 새로운 최빈값을 찾으면 배열 초기화
        } else if (counter[key] === maxCount) {
            maxElements.push(key); // 같은 최빈값이 있으면 추가
        }
    }
    
    // 최빈값이 여러 개일 경우 -1 반환
    if (maxElements.length > 1) {
        return -1;
    }
    
    // 최빈값 반환
    return parseInt(maxElements[0]); // 최빈값을 정수로 반환
}
