#Problem 2405 of LeetCode
class Solution:
    def partitionString(self, s: str) -> int:
        partitions = []
        currentString = ''
        for char in s:
            if char not in currentString:
                currentString += char
            else:
                partitions.append(currentString)
                currentString = ''+char
        if currentString != '':
            partitions.append(currentString)
        return len(partitions)
