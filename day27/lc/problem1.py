# 3120. Count the Number of Special Characters I


def numberOfSpecialChars(word):
    seen=set()
    ans=0
    for i in word:
        temp=i.upper()
        if i.isupper():
            temp=i.lower()
        if temp not in seen:
            if i not in seen:
                seen.add(i)
        else:
            if i not in seen:
                ans+=1
                seen.add(i)
    return ans

word = "abc"
print(numberOfSpecialChars(word))