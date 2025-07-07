function solution(answers) {
    var stdAnswer = [];
    let count = [0,0,0];
    const student = [[1,2,3,4,5],
                     [2,1,2,3,2,4,2,5],
                    [3,3,1,1,2,2,4,4,5,5]
                    ];
    
    answers.forEach((answer, ansIdx)=>{
        //2중 배열인 student를 돔 
        student.forEach((std, stdIdx)=>{
            if(answer == std[ansIdx%std.length]){
                count[stdIdx]++
            }  
        })
    })
    //가장 큰 수의 인덱스
    let stdMax = Math.max(...count)
    count.forEach((value, index)=>{
        if(value == stdMax){
            stdAnswer.push(index+1)
        }              
    })
    
    return stdAnswer;
}