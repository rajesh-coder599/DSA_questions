# 3751. Total Waviness of Numbers in Range I


def totalWaviness(num1,num2):
    ans=0
    for i in range(num1,num2+1):
        if i<100:
            continue
        s=str(i)
        l=len(s)
        for j in range(1,l-1):
            x=int(s[j-1])
            y=int(s[j])
            z=int(s[j+1])
            if x<y>z or x>y<z:
                ans+=1
    return ans

n1=4848
n2=4848
print(totalWaviness(n1,n2))