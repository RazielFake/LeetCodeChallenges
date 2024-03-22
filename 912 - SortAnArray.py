#Problem 912 of LeetCode implementing MergeSort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

        

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        sortArr = []
        while left and right:
            if left[0] < right[0]:
                sortArr.append(left[0])
                left.pop(0)
            else:
                sortArr.append(right[0])
                right.pop(0)
        sortArr.extend(left)
        sortArr.extend(right)
        
        return sortArr
        
