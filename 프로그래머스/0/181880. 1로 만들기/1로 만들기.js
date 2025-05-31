function solution(num_list) {
    var answer = 0;
    answer = num_list.map(_=>{
        let count=0;
        while(_!=1){
            _= _%2==0? _/2: (_-1)/2;
            count++
        }
        return count;
    })
    return answer.reduce((cur,ans)=>cur+ans);
}