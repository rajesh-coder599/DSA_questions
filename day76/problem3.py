# 3876. Construct Uniform Parity Array II



def uniformArray(nums1):
    odd_count=0
    even_count=0
    mn_odd=float("inf")
    mn_even=float("inf")
    for i in nums1:
        if i%2==0:
            even_count+=1
            mn_even=min(mn_even,i)
        else:
            odd_count+=1
            mn_odd=min(mn_odd,i)
    if odd_count==0 or even_count==0:
        return True
    if mn_even%2==0 and abs(mn_even-mn_odd)<1:
        return True
    return False


## 2nd method
def uniformArray(nums1):
    mn=min(nums1)
    if mn%2==1:
        return True
    for i in nums1:
        if i%2==1:
            return False
    return True