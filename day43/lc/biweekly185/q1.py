# Q1. Create Grid With Exactly One Path©leetcode


def createGrid(m,n):
    a=["."]*n
    b=["#"]*n
    b[-1]="."
    u="".join(a)
    s="".join(a)
    grid=[s]
    for _ in range(m-1):
        grid.append(u)
    return grid
m=2
n=3
print()