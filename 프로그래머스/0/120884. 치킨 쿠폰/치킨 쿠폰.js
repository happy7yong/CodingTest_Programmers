function solution(chicken) {
    var left_coupon = 0;
    var service = 0;
    var new_coupon = 0;
    
    while(chicken>=10){
        new_coupon = Math.floor(chicken/10)
        service += new_coupon
        left_coupon = chicken%10
        chicken = left_coupon+new_coupon
    }
    return service;
}