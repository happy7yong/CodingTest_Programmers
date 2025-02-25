function solution(n) {
    var counter = 0;
    var count = 0;
    
    while(count<n){
        counter++;
        
        if(counter%3==0 || counter.toString().includes("3")){
            continue;
        }
        count++
    }
    
    return counter;
}