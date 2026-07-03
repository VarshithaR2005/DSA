class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        gcd=1
        if(mini%mini==0 and maxi%mini==0):
            return mini
        else:
            for i in range(mini-1,0,-1):
                if(maxi%i==0 and mini%i==0):
                    gcd=i
                    break
        return gcd


