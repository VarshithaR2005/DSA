class Solution:
	def closestPalindrome(self, num):
		# code here
		n = len(num)
        if num == num[::-1]:
            return num
        def make_pal(prefix, odd):
            if odd:
                return prefix + prefix[:-1][::-1]
            return prefix + prefix[::-1]
        half = (n + 1) // 2
        prefix = int(num[:half])
        candidates = set()
        for x in [prefix - 1, prefix, prefix + 1]:
            if x <= 0:
                continue
            p = str(x)
            candidates.add(make_pal(p, n % 2))
        candidates.add("9" * (n - 1))
        candidates.add("1" + "0" * (n - 1) + "1")
        original = int(num)
        ans = None
        for p in candidates:
            if len(p) == 0:
                continue
            val = int(p)
            if ans is None:
                ans = val
            else:
                if abs(val - original) < abs(ans - original):
                    ans = val
                elif abs(val - original) == abs(ans - original):
                    ans = min(ans, val)
        return str(ans)
