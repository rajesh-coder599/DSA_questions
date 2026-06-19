# 1732. Find the Highest Altitude


def largestAltitude(gain):
    arr=[0]
    for i in gain:
        temp=arr[-1]+i
        arr.append(temp)
    return max(arr)