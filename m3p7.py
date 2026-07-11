class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        n1=bin(n)[2:]
        n=bin(n)[2:]
        n1=n1[::-1]
        if(n==n1):
            return True
        else:
            return False