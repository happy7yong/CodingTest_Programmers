nums = list(map(int, input().split()))

arr_mock = [0]*15
p = 0


nums.sort()
n = len(nums)

a_a,a_b,a_c,a_d = 0,0,0,0

def condition(a,b,c,d) :
    arr_mock[4] = a+b
    arr_mock[5] = b+c
    arr_mock[6] = c+d
    arr_mock[7] = d+a
    arr_mock[8] = a+c
    arr_mock[9] = b+d
    arr_mock[10] = a+b+c
    arr_mock[11] = a+b+d
    arr_mock[12] = a+c+d
    arr_mock[13] = b+c+d
    arr_mock[14] = a+b+c+d
    #집합으로 바꾸기 
        

for a in range(0,n) :
    for b in range(a+1,n) :
        for c in range(b+1,n) :
            for d in range(c+1,n) :
                #초기화
                arr_mock = [0]*15
                arr_mock[0]=nums[a]
                arr_mock[1]=nums[b]
                arr_mock[2]=nums[c]
                arr_mock[3]=nums[d]
                condition(nums[a],nums[b],nums[c],nums[d])
                arr_mset=set(arr_mock)
                nums_mset = set(nums)
                if arr_mset == nums_mset :
                    a_a = nums[a]
                    a_b = nums[b]
                    a_c = nums[c]
                    a_d = nums[d]
                

print(a_a,a_b,a_c,a_d)
