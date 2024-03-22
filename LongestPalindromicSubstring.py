#Problem 5 of LeetCode
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        lenAns = 0
        
        for n in range(len(s)):
            left, right = n, n
            #ODD palyndromes
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > lenAns:
                    ans = s[left:right+1]
                    lenAns = right - left + 1
                left-=1
                right+=1
            #EVEN palyndromes
            left, right = n, n+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > lenAns:
                    ans = s[left:right+1]
                    lenAns = right - left + 1
                left-=1
                right+=1

        
        return ans
