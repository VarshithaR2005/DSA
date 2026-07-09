class Solution:
	def powerSet(self, s):
		# Code here
		res=[]
		n=len(s)
		for i in range(1<<n):
		    subsequence=""
		    for j in range(n):
		        if(i&(1<<j)):
		            subsequence+=s[j]
		    res.append(subsequence)
	    res.sort()
	    return res
		            
		            
		        
		