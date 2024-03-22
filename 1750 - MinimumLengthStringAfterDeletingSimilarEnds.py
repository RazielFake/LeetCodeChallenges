#Problem 1750 of LeetCode
class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        while True:
            if s[0] != s[len(s)-1] or len(s) == 1:
                return len(s)
            else:
                currentChar = s[0]
            
            while s[0] == currentChar:
                s.pop(0)
                if not s:
                    return len(s)
            while s[len(s)-1] == currentChar:
                s.pop()
                if not s:
                    return len(s)
            
        return len(s)
