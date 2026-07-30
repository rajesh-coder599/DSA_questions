# https://codeforces.com/problemset/problem/271/A
# A. Beautiful Year


y=input()
while True :
    y=str(int(y)+1)
    if y[0] not in {y[1],y[2],y[3]} and y[1] not in {y[2],y[3]} and y[2] != y[3] :
        break
print(int(y))