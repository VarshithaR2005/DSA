class Solution:
    def bestNumbers(self, n, a, b, c, d):
        # code here
        MOD = 10**9 + 7
        def good(x):
            while x > 0:
                digit = x % 10
                if digit == c or digit == d:
                    return True
                x //= 10
            return False
        if a == b:
            return 1 if good(n * a) else 0
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % MOD
        invFact = [1] * (n + 1)
        invFact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD
        ans = 0
        for k in range(n + 1):
            digit_sum = (n - k) * a + k * b
            if good(digit_sum):
                ways = fact[n]
                ways = (ways * invFact[k]) % MOD
                ways = (ways * invFact[n - k]) % MOD
                ans = (ans + ways) % MOD
        return ans
