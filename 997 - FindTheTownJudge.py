'''
Problem 997 of LeetCode
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustin = [0] * (n + 1)
        trusted = [0] * (n + 1)
        for element in trust:
            trusted[element[0]] += 1
            trustin[element[1]] += 1
        for k in range(1, n + 1):
            if trustin[k] == n-1 and trusted[k] == 0:
                return k
        return -1
