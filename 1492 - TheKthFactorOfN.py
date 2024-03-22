#Problem 1492 of LeetCode
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [i for i in range(1,n+1) if n%i == 0]
        if k > len(factors):
            return -1
        else:
            return factors[k-1]
