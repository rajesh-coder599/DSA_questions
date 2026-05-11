# Bear and Candies 123

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    
    k=int(a**0.5)
    if b>=k*(k+1):
        print("Bob")
    else:
        print("Limak")

