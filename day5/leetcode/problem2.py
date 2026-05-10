# 22. Genrate parantheses

n=5
def genrate(n):
    ans=[]
    def parentheses(open_count,close_count,curr,limit):
        if open_count==close_count==limit:
            ans.append(curr)
            return
        if open_count<limit:
            parentheses(open_count+1,close_count,curr+"(",limit)
        if open_count>close_count:
            parentheses(open_count,close_count+1,curr+")",limit)

        
        

    parentheses(0,0,"",n)
    return ans

print(genrate(n))
        
