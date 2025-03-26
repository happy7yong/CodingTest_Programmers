function solution(wallpaper) {
    var answer = [];
    var Sx=[], Sy = [];
    
    for(let row=0;row<wallpaper.length;row++){
        answer[row]=[...wallpaper[row]]
    }   
    
    for(let i=0;i<wallpaper.length;i++){
        for(let j=0;j<wallpaper[0].length;j++){
            if(answer[i][j]=="#"){
                Sx.push(i)
                Sy.push(j)
            }   
        }
    }
    
    console.log(Sx,Sy)
    return [Math.min(...Sx),Math.min(...Sy),Math.max(...Sx)+1,Math.max(...Sy)+1];
}