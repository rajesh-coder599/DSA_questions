# 3871. Count Commas in Range II



def countCommas(n):
    if n<1000:
        return 0
    ans=0
    x=1000
    while n>999:
        ans+=(n-x+1)
        x*=1000
    return ans