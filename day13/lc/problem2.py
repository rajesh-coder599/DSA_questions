# 796. Rotate String

def rotateString(s, goal):
    n=len(s)
    if n!=len(goal):
        return False
    a=s+s
    if goal in a:
        return True
    return False

s="abcde"
g="cdeab"
print(rotateString(s,g))