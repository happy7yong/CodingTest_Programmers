function solution(array, commands) {
    var answer = [];
    var slice=[];
    for(let i=0;i<commands.length;i++){
            slice=array.slice(commands[i][0]-1,commands[i][1])
            slice.sort((a,b)=>a-b)
        console.log(slice)
            answer.push(slice[commands[i][2]-1]);
        console.log(answer)
        console.log("1")
    }
    return answer;
}