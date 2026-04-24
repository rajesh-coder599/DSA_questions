# 2833. Furthest Point From Origin
moves="L_RL__R"
n=len(moves)
left=0
right=0
for i in moves:
    if i=="L" :
        left+=1
    elif i=="R" :
        right+=1
    else:
        left+=1
        right+=1

a=max(left,right)
print(a-n+a)