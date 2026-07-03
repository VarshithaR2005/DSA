class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<=2):
            return 0
        arr=[True]*n
        arr[0]=arr[1]=False
        i=2
        while i*i<n:
            if arr[i]:
                j=i*i
                while(j<n):
                    arr[j]=False
                    j+=i
            i+=1
        return sum(arr)

        