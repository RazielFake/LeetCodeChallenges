#Problem 1122 of LeetCode
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #return sorted(arr1, key=lambda x:(x not in arr2, arr2.index(x) if x in arr2 else x))
        numsIn = []
        numsOut = []
        for num in arr1:
            if num in arr2:
                numsIn.append(num)
            else:
                numsOut.append(num)
        ans = sorted(numsIn, key = lambda x: arr2.index(x))
        ans.extend(sorted(numsOut))
        return ans
