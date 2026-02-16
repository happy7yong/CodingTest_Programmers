
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

function solution(n,arr){
    //정수를 저장하는 큐 구현
    let queue = []; //큐
    let answer = []; //답안지

    for(let i of arr){
        let [command, n] = i.split(" ");
        Number(n);
        // console.log(command,n);
        

        switch(command){
            case "push" :
                queue.push(n);
                break;
            case "pop" :
                let q = queue.shift();
                answer.push(q ? q : -1);
                break;
            case "front":
                answer.push(queue[0] ? queue[0] : -1);
                break;
            case "back":
                answer.push(queue[queue.length-1] ? queue[queue.length-1] : -1)
                break;
            case "empty":
                answer.push(queue.length === 0 ? 1 : 0);
                break;
            case "size":
                answer.push(queue.length);
                break;

        }

        // console.log("queue", queue);
        // console.log("answer", answer);


    }


    return answer;

}



const n = Number(input[0].split(" ")[1]);
let arr = input.splice(1);

console.log(solution(n,arr).join("\n"));