class Solution:
    def reverseexponentiation(self, n):
        # code here
        s=str(n)
        s=s[::-1]
        n1=int(s)
        return pow(n,n1)
        