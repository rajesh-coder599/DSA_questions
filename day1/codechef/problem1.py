# Easy Pronunciation

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    vowels={"a":"a",
        "e":"e",
        "i":"i",
        "o":"o",
        "u":"u"
    }
    x=0
    for i in s:
        if x==4 :
            break
        if i in vowels :
            x=0
        else:
            x+=1
    if x==4 :
        print("NO")
    else:
        print("YES")