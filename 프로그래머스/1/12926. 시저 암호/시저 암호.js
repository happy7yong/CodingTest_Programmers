function solution(s, n) {
    //a를 밀어서 
    var answer = '';
    let char = 0;
    upperChar = 65; //A가 인덱스 0이 되어야하나 
    lowerChar = 97;
    console.log('Z'.charCodeAt(0)) // A :65, Z:90 / a : 97, z:122 : 26개  
    //charCodeAt <-> fromCharCode
    for(let i=0;i<s.length;i++){
        if(s[i] == ' '){
            answer+=' ';   
        }else if(isUpper(s[i])){//대문자일 때
            //항상64를뺌 
            char = (s.charCodeAt(i)-upperChar+n)%26
            answer += String.fromCharCode(char+upperChar)
        }else if(isLower(s[i])){//소문자일 때
            char = (s.charCodeAt(i)-lowerChar+n)%26
            answer += String.fromCharCode(char+lowerChar)
        }
    }
    return answer
}

function isUpper(char){
    if(char>='A' && char<= 'Z'){
        return true
    }
    
    return false
}

function isLower(char){
    if(char>='a'&&char<='z'){
        return true
    }
    
    return false
}