# 3477. Fruits Into Baskets II



def numOfUnplacedFruits(fruits,baskets):
    n=len(fruits)
    used=set()
    ans=0
    for i in fruits:
        check=False
        for j in range(n):
            if baskets[j]>=i and j not in used:
                used.add(j)
                check=True
                break
        if not check:
            ans+=1
    return ans