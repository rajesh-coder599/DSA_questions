# 344A. magnets

n=int(input())
prev=None
group=1
for i in range(n):
    pol=input()
    if prev==None:
        prev=pol
        continue
    if pol != prev:
        group+=1
        prev=pol

print(group)