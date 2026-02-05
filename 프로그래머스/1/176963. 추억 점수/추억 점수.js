function solution(name, yearning, photo) {
    //사진별로 추억의 점수 매긴댑니다.
    //그리움의 점수를 모두 합산 
    //name : 그리워하는 사람의 이름을 담은 문자열
    //yearning : 사람별 그리움 점수 
    //photo : 사진에 찍힌 인물의 이름을 담은 배열
    
    //name -> yearning 을 매핑해야됨.
    let nameScoreMap = {};
    let answer = [];
    let score = 0;
    
    name.forEach((item,idx) => nameScoreMap[item] = yearning[idx]);
    
    photo.map(photoSnap=>{
        photoSnap.forEach(i=>score+=nameScoreMap[i] || 0 );
        console.log(score);
        answer.push(score);
        score=0;
    })
    
    return answer;
}