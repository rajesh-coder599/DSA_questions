# 3908. Valid Digit Number

n = 101
x = 2
digit=False
while n>9:
    temp=n%10
    n//=10
    if temp==x:
        digit=True
if digit==False or n == x :
    print(False)
else:
    print(True)

