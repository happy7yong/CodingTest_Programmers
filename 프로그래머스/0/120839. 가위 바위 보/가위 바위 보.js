function solution(rsp) {
    var answer = '';
    var rsp_arr = [...rsp]
    for(let i=0;i<rsp_arr.length;i++){
        switch(rsp_arr[i]){
            case "2":
                rsp_arr[i]="0"
                break;
            case "0" :
                rsp_arr[i]="5"
                break;
            case "5" :
                rsp_arr[i]="2"
                break;
        }   
    }
    answer=rsp_arr.join("")
    
    
    return answer;
}