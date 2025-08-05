function solution(myString, pat) {
    //뒤에서부터 찾아야됨 
    var answer = 0;
    answer = myString.lastIndexOf(pat)
    
    //인덱스+길이까지 Slice
    var resultString= myString.slice(0,answer+pat.length)
    
    return resultString;
}