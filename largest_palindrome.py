import math
def palindrome(maxInt):
    maxpal=0
    for x in range(maxInt,0,-1):
        if x*x<maxpal:
            break
        for y in range(x,max(maxpal//x,10**int(math.log10(x))-1),-1):
            num=x*y
            if str(num) == str(num)[::-1]:
                maxpal=num
                break
    return maxpal
