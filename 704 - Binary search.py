#Probleme 704 of LeetCode
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        def binarySearch(left, right, array, target):
            if right >= left:
                mid = (right+left)//2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    return binarySearch(left, mid-1, array, target)
                elif array[mid] < target:
                    return binarySearch(mid+1, right, array, target)
            else:
                return -1
        return binarySearch(0, len(nums), nums, target)
