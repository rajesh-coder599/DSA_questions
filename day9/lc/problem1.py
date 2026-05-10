# 3707. Equal score substring

s="ayz"
def scorebalance(s):
    n=len(s)
    score={
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26
    }

    total_score=0
    for i in s:
        total_score+=score[i]

    if total_score%2 != 0 :
        return False
    
    a=total_score//2
    for i in range(n):
        a-=score[s[i]]
        if a<=0:
            if a==0:
                return True
            else:
                return False
    
print(scorebalance(s))