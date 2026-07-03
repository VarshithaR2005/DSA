class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        ans=x
        res=1
        while n!=0:
            if n&1==1:
                res=res*ans
            ans=ans*ans
            n=n>>1
        return(res)
    print(myPow)