function solution(board) {
    var board_cl = board.map((row)=>[...row]);
    for(let i=0;i<board.length;i++){
        board[i].map((num,index)=> {
            if(num==1) { 
                board_cl[i][index-1]=1; 
                board_cl[i][index+1]=1;
                if(i>0) {
                    board_cl[i-1][index]=1;
                    board_cl[i-1][index+1]=1;
                    board_cl[i-1][index-1]=1;
                }
                if(i<board.length-1){
                    board_cl[i+1][index]=1;
                    board_cl[i+1][index+1]=1;
                    board_cl[i+1][index-1]=1;
                }
            }
        })   
    }
    
    var board_ans = board_cl.map((row)=>row.filter((num)=>num!==1))
    board_ans = board_ans.map((row)=>row=row.length).reduce((acc,cur)=>acc+cur)
    return board_ans;
}