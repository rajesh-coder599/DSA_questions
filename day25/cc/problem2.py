# Yet another SOD problem


t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    print(r//3-l//3+(1 if l%3==0 else 0))