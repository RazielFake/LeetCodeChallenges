#Problem 394 of LeetCode
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        num = ''
        for idx, char in enumerate(s):
            if char.isdigit():
                num += char
            if char == '[':
                stack.append(ans)
                stack.append(int(num))
                num = ''
                ans = ''
            elif char.isalpha():
                ans += char
            elif char == ']':
                multiplier = stack.pop()
                ans = stack.pop() + (ans * multiplier)
                print(ans)

        print(ans)
        return ans
