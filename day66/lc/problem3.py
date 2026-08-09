# 4014. Minimum Total Price After Applying Discounts



def minPrice(prices,discounts):
    prices.sort(reverse=True)
    discounts.sort(reverse=True)
    ans=0
    n=len(prices)
    m=len(discounts)
    for i in range(len(prices)):
        if i>=m:
            ans+=prices[i]
            continue
        d=discounts[i]
        ans+=(prices[i]*(100-d))/100
    return ans