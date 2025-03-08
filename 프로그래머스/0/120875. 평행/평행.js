function solution(dots) {
    var dots_A = (dots[0][1]-dots[1][1])/(dots[0][0]-dots[1][0])
    var dots_AE = (dots[2][1]-dots[3][1])/(dots[2][0]-dots[3][0])
    if(dots_A==dots_AE)
        return 1;
    
    var dots_B = (dots[0][1]-dots[2][1])/(dots[0][0]-dots[2][0])
    var dots_BE = (dots[1][1]-dots[3][1])/(dots[1][0]-dots[3][0])
    if(dots_B==dots_BE)
        return 1;
    
    var dots_C = (dots[0][1]-dots[3][1])/(dots[0][0]-dots[3][0])
    var dots_CE = (dots[1][1]-dots[2][1])/(dots[1][0]-dots[2][0])
    if(dots_C==dots_CE)
        return 1;

    return 0;
}