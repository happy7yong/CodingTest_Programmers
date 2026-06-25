n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class Address :
    def __init__(self,name,street_address,region):
        self.name = name
        self.address = street_address
        self.region = region

address_arr = []
for i in range(n) :
    address_arr.append(Address(name[i],street_address[i],region[i]))

name.sort()
answer_object = ""

for ele in address_arr :
    if ele.name == name[-1] :
        answer_object = ele

print("name",answer_object.name)
print("addr",answer_object.address)
print("city",answer_object.region)

