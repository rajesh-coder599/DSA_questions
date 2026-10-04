# 678. Valid Parenthesis String



def checkValidString(s):
    a=[]
    counter=0
    for i in s:
        if i==")":
            if len(a)==0:
                return False
            if counter>0:
                a=a[::-1]
                a.remove("(")
                a=a[::-1]
                counter-=1
            else:
                a.pop()
        else:
            a.append(i)
            if i=="(":
                counter+=1
    flag=0
    for i in a[::-1]:
        if i=="*":
            flag+=1
        else:
            if flag==0:
                return False
            flag-=1
    return True