# String Game

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    zeros=0
    ones=0
    for i in s:
        if i=="1":
            ones+=1
        else:
            zeros+=1
    
    a=min(zeros,ones)
    if a%2==0:
        print("Ramos")
    else:
        print("Zlatan")