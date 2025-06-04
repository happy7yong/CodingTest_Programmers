function solution(n, slicer, num_list) {
    var answer = [];
    let start = n==1 ? 0 : slicer[0] 
    let end = n==2 ? num_list.length : slicer[1]+1
    let interval = n==4 ? slicer[2] : 1;
    
    answer = num_list.slice(start,end)
    answer = answer.filter((_,i)=>i%interval==0)
    
    return answer;
}