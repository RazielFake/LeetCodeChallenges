#Problem 791 of LeetCode
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDict = {}
        for idx, char in enumerate(order):
            orderDict[char] = idx
        return ''.join(sorted(s, key=lambda x:orderDict.get(x,100)))
