# Correct Sentence

t=int(input())
for _ in range(t):
    arr=input().split()
    k=int(arr[0])
    words=arr[1:]
    check=True
    for i in range(k):
        s=words[i]
        if not check :
            break
        if not s.islower() and not s.isupper():
            check=False
        if s.isupper():
            for j in s:
                if ord(j)<78:
                    check=False
        if s.islower():
            for j in s:
                if ord(j)>109:
                    check=False
    if check:
        print("YES")
    else:
        print("NO")