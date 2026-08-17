# 406. Queue Reconstruction by Height



def reconstructQueue(people):
    people.sort(key=lambda x: (-x[0],x[1]))
    ans=[]
    for h,k in people:
        ans.insert(k,[h,k])
    return ans