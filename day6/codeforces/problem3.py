# 271A. Beautiful year

year=input()
year=str(int(year)+1)
loop=True
while loop:
    newy=""
    loop=False
    for i in year:
        if i in newy:
            newy+=i
            newy=str(int(newy)+1)
            loop=True
        else:
            newy+=i
    year=newy

print(year)