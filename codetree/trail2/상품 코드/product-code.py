product_name, product_code = input().split()
product_code = int(product_code)

class Product :
    def __init__(self,product_name, product_code) :
        self.name = product_name
        self.code = product_code

product1 = Product("codetree", 50)
product2 = Product(product_name, product_code)

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")