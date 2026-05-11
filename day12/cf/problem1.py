# 2143B. Discounts

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    product=list(map(int,input().split()))
    discount=list(map(int,input().split()))
    product.sort()
    product=product[::-1]
    discount.sort()
    total_cost=sum(product)
    l=0
    for i in discount:
        if l+i>n:
            break

        total_cost-=min(product[l:i+l])
        l+=i
    print(total_cost)