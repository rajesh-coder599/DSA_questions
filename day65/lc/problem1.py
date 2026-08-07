# 3348. Smallest Divisible Digit Product II


## WA (i will )
def smallestNumber(num,t):
    def prime(i):
        if i==2:
            return [2,1]
        elif i==3:
            return [3,1]
        elif i==4:
            return [2,2]
        elif i==5:
            return [5,1]
        elif i==7:
            return [7,1]
        elif i==8:
            return [2,3]
        else:
            return [3,2]
    from collections import defaultdict
    n=len(num)
    possible_prime=[2,3,5,7]
    prime_of_t_freq=defaultdict(int)
    i=0
    x=t
    while i<4:
        if x%possible_prime[i]==0:
            x//=possible_prime[i]
            prime_of_t_freq[possible_prime[i]]+=1
        else:
            i+=1
    if x!=1:
        return "-1"
    prime_of_num_freq=defaultdict(int)
    for i in num:
        i=int(i)
        if i>1:
            if i==6:
                prime_of_num_freq[2]+=1
                prime_of_num_freq[3]+=1
            else:
                v,f=prime(i)
                prime_of_num_freq[v]+=f
    freq_diff={}
    freq_diff[2]=prime_of_t_freq[2]-prime_of_num_freq[2]
    freq_diff[3]=prime_of_t_freq[3]-prime_of_num_freq[3]
    freq_diff[5]=prime_of_t_freq[5]-prime_of_num_freq[5]
    freq_diff[7]=prime_of_t_freq[7]-prime_of_num_freq[7]
    ans=""
    for i in range(n-1,-1,-1):
        x=int(num[i])
        if x>1:
            if x==6:
                freq_diff[2]+=1
                freq_diff[3]+=1
            else:
                v,f=prime(x)
                freq_diff[v]+=f
        if freq_diff[3]>1:
            freq_diff[3]-=2
            ans="9"+ans
        elif freq_diff[2]>2:
            freq_diff[2]-=3
            ans="8"+ans
        elif freq_diff[7]>0:
            freq_diff[7]-=1
            ans="7"+ans
        elif freq_diff[2]>0 and freq_diff[3]>0:
            freq_diff[2]-=1
            freq_diff[3]-=1
            ans="6"+ans
        elif freq_diff[5]>0:
            freq_diff[5]-=1
            ans="5"+ans
        elif freq_diff[2]>1:
            freq_diff[2]-=2
            ans="4"+ans
        elif freq_diff[3]>0:
            freq_diff[3]-=1
            ans="3"+ans
        elif freq_diff[2]>0:
            freq_diff[2]-=1
            ans="2"+ans
        else:
            if x==0:
                ans="1"+ans
            else:
                ans=num[i]+ans
    remaining_prime=[]
    for k,v in freq_diff.items():
        temp=[]
        if v>0:
            if k==2:
                if v>2:
                    x=v//3
                    v=v%3
                    for i in range(x):
                        temp.append(8)
                if v>0 and freq_diff[3]%2==1:
                    temp.append(6)
                    v-=1
                    freq_diff[3]-=1
                if v==2:
                    v=0
                    temp.append(4)
                if v==1:
                    temp.append(2)
            if k==3:
                if v>1:
                    x=v//2
                    v=v%2
                    for i in range(x):
                        temp.append(9)
                if v==1 and freq_diff[2]>0:
                    temp.append(6)
                    freq_diff[2]-=1
                    v=0
                if v==1:
                    temp.append(3)
            if k==5:
                for i in range(v):
                    temp.append(5)
            if k==7:
                for i in range(v):
                    temp.append(7)
        remaining_prime.extend(temp)
    remaining_prime.sort()
    if remaining_prime:
        a=""
        for i in remaining_prime:
            a+=str(i)
        ans=a+ans
    while int(ans)<int(num):
        ans="1"+ans
    return ans

num="17"
t=252047376
print(smallestNumber(num,t))