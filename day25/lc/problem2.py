
# Q2. Password Strength©leetcode

def passwordStrength(password):
    a=set()
    b={"!","@","#","$"}
    ans=0
    for i in password:
        if i not in a:
            if i in b:
                ans+=5
                a.add(i)
            elif i.isdigit() :
                ans+=3
                a.add(i)
            elif i.islower():
                ans+=1
                a.add(i)
            else:
                ans+=2
                a.add(i)
    
    return ans

s="aA1!"
print(passwordStrength(s))