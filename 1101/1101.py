product = 0
product_price = 0
n, d = map(int,input('').split(' '))
for i in range(n):
    product_list = [int(i) for i in input('').split(' ')]
    if max(product_list) - min(product_list) >= d:
        product += 1
        product_price += int(sum(product_list)/len(product_list))
print(f'{product} {product_price}')