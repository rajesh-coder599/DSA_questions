# Chef and Subarray

n=int(input())
arr=list(map(int,input().split()))
mx_len=0
curr_len=0
for i in arr:
    if i==0:
        curr_len=0
        continue
    curr_len+=1
    mx_len=max(curr_len,mx_len)

print(mx_len)