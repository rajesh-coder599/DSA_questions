# 3612. Process String with Special Operations I


def processStr(s):
    ans=""
    for i in s:
        if 97<=ord(i)<=122 :
            ans+=i
        else:
            if i=="%":
                ans=ans[::-1]
            if i=="#":
                ans+=ans
            if i=="*":
                ans=ans[:-1]
    return ans