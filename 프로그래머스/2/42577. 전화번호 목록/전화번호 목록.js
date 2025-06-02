function solution(phone_book) {
    //set에 먼저 넣기
    let book = new Set(phone_book);
    
    for(let number of phone_book){
        let prefix = "";
        for(let i=0;i<number.length-1;i++){
            prefix += number[i];
            if(book.has(prefix))
                return false
        }
    }
    return true;

}