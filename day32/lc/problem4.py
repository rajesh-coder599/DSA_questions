# Q4. Lexicographically Maximum MEX Array


def maximumMEX(nums):
    ans=[]
    freq={}
    for i in nums:
        if i not in nums:
            freq[i]=1
        else:
            freq[i]+=1
    prevmex=None
    for i in freq:
        if prevmex==None:
            if i!=0:
                prevmex=0
            else:
                prevmex=1
            freq[i]-=1
        else:
            if i==prevmex:
                prevmex+=1
                freq[i]-=1
        
        if prevmex not in freq or freq[prevmex]!=0 :
            ans.append(prevmex)
            prevmex=None
    return ans