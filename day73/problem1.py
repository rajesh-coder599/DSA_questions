# 4031. Find All Numbers Disappeared in an Array II




def findDisappearedNumbers(nums,lower,upper):
    st=None
    end=None
    a=set(nums)
    ans=[]
    for i in range(lower,upper+1):
        if i not in a:
            if st==None:
                st=i
                end=i
            else:
                end=i
        else:
            if st!=None:
                ans.append([st,end])
                st=None
                end=None
    if st!=None:
        ans.append([st,end])
    return ans