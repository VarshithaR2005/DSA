class Solution:
    def gcd(self, n, arr):
        # code here 
        mini=min(arr)
        count=0
        for num in arr:
            if(num%mini==0):
                count+=1
        if count==n:
            return mini
        count=0
        for i in range(mini-1,0,-1):
            count=0
            for num in arr:
                if(num%i==0):
                    count+=1
            if(count==n):
                return i
        return mini
            
        