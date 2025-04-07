function solution(todo_list, finished) {
    var answer = [];
    return todo_list.filter((num,index)=>!finished[index]);
}