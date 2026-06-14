inputList = list(map(int,input().split()))

fillter_odd = inputList[::2]
fillter_even = inputList[1::2]
odd_val = sum(fillter_odd)
even_val = sum(fillter_even)
max_val = max(odd_val,even_val)
min_val = min(odd_val,even_val)

print(max_val-min_val)
