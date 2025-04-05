function solution(arr1, arr2) {
    var answer = 0;
    if(arr1.length != arr2.length){
        if(arr1.length < arr2.length){
            answer = -1;
        }else if(arr1.length > arr2.length){
            answer = 1;
        }
    }else if(arr1.length == arr2.length){
        answer = arr1.reduce((acc,rec)=>acc+rec) > arr2.reduce((acc,rec)=>acc+rec) ? 1 : 
            arr1.reduce((acc,rec)=>acc+rec) == arr2.reduce((acc,rec)=>acc+rec) ? 0 : -1 
        
    }
    return answer;
}