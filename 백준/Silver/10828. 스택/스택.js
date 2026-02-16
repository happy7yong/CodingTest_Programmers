
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");


function solution(n,arr){
    //정수를 저장하는 큐 구현
    let stack = []; //큐
    let answer = []; //답안지

    for(let i of arr){
        let [command, n] = i.split(" ");
        Number(n);
        // console.log(command,n);
        

        switch(command){
            case "push" :
                stack.push(n);
                break;
            case "pop" :
                let s = stack.pop();
                answer.push(s ? s : -1);
                break;
            case "top":
                answer.push(stack[stack.length-1] ? stack[stack.length-1] : -1);
                break;
            case "empty":
                answer.push(stack.length === 0 ? 1 : 0);
                break;
            case "size":
                answer.push(stack.length);
                break;

        }

        // console.log("stack", stack);
        // console.log("answer", answer);


    }


    return answer;

}



const n = Number(input[0].split(" ")[1]);
let arr = input.splice(1);

console.log(solution(n,arr).join("\n"));

