function solution(chicken) {
    let service = 0;
    let coupon_left = 0;
    
    while( chicken>=10 ){
        let coupon_new = Math.floor(chicken/10);
        service += coupon_new;
        coupon_left = chicken%10
        chicken = coupon_left+coupon_new
    }
    
    return service;
}