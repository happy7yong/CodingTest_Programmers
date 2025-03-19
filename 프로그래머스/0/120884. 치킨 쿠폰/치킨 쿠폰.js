const chicken_couponer = (chicken_coupon) =>{
    var coupon_remain = 0;
    var chicken_cur = 0;
    
     while(chicken_coupon>0){
        chicken_cur+=Math.floor(chicken_coupon/10); //치킨
        coupon_remain+=chicken_coupon%10 //치킨 쿠폰 나머지
        chicken_coupon=Math.floor(chicken_coupon/=10)
        
    
    }
    return [coupon_remain,chicken_cur];
    
}

function solution(chicken_coupon) {
    var chicken = 0;
    var coupon_remain = 0;
    
    [coupon_remain, chicken] = chicken_couponer(chicken_coupon)

    while(coupon_remain >= 10) {
        let chicken_method = chicken_couponer(coupon_remain)
        coupon_remain = chicken_method[0]
        chicken += chicken_method[1]
    }
    
    
    return chicken;
}