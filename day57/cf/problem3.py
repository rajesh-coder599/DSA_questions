# https://codeforces.com/problemset/problem/2225/C
# C. Red-Black Pairs



t=int(input())
for _ in range(t):
    n=int(input())
    colour=[input() for _ in range(2)]
    skip=False
    changecolour=0
    for i in range(n):
        if skip:
            skip=False
            continue
        if i<n-1 and colour[0][i]==colour[0][i+1] and colour[1][i]==colour[1][i+1] :
            skip=True
        elif colour[0][i]==colour[1][i] :
            continue
        elif i<n-1 and (colour[0][i]==colour[0][i+1] or colour[1][i]==colour[1][i+1]): 
            changecolour+=1
            skip=True
        else:
            changecolour+=1
    print(changecolour)