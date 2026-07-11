class Solution:
    def isPowerofTwo(self, n):
        # code here
        # if(n&(n-1)==0):
        #     return True
        # else:
        #     return False
        b=bin(n)[2:]
        l=b.count("1")
        if(l==1):
            return True
        else:
            return False
        