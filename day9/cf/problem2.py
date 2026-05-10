# 2182A. new year string

t=int(input())
for _ in range(t):
    s=input()
    if "2026" in s:
        print(True)
    elif "2025" not in s:
        print(True)
    else:
        print(False)

