class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aa=int(a,2)
        bb=int(b,2)
        sum=aa+bb
        return(bin(sum)[2:])
        