# 2227B. party monster

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    open_cont=0
    close_count=0
    for i in s:
        if i=="(" :
            open_cont+=1
        else:
            close_count+=1

    if open_cont==close_count:
        print("YES")
    else:
        print("NO")