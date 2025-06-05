function solution(survey, choices) {
    let result = '';
    
    //해시
    let type = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    
    for(let i=0;i<survey.length;i++){
        //구조 분해 할당
        let [first, second]= survey[i];
        let choice = choices[i]
        
        if(choice < 4){
            type[first] += 4- choice
        }else if(choice > 4){
            type[second] += choice-4 
        }
        
        
    }
    
    
    //여기서부터가 어려움.
    let pairs = [['R','T'],['C','F'],['J','M'],['A','N']]
    for(const [a,b] of pairs){
        result += type[a] >= type[b] ? a : b;
    }
    
    
    return result;
}