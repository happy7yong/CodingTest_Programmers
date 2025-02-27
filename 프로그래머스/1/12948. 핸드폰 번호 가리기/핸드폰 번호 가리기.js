function solution(phone_number) {
    var phone_num = phone_number.length
    var num_stack = []
    for(let i=0;i<phone_num;i++){
        if(i>=phone_num-4){
            num_stack+=phone_number[i]
        }else{
            num_stack+="*"
        }
    }
    return num_stack;
}