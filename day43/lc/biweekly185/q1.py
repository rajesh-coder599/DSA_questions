# Q1. Create Grid With Exactly One Path©leetcode


def createGrid(m,n):
    a=["."]*n
    b=["#"]*n
    u="".join(a)
    s="".join(a)
    grid=[s]
    for _ in range(m-1):
        temp=u[:0]+"."
        grid.append(temp)
    return grid