# 1967. Number of Strings That Appear as Substrings in Word



def numOfStrings(patterns,word):
    ans=0
    for i in patterns:
        if i in word:
            ans+=1
    return ans