# Zero String

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    zeros=s.count("0")
    ones=s.count("1")
    if zeros>=ones:
        print(ones)
    else:
        print(zeros+1)