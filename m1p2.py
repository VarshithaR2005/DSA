class Solution:
    def isPrime(self, n):
        # code here
        flag=True
        if n==1:
            return False
        else:
            for i in range(2,n):
                if(n%i==0):
                    flag=False
                    break
            if(flag):
                return True
            return False
        