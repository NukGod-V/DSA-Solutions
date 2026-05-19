class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < (len(nums)-1):
            j = i + 1
            rem = target - nums[i]
            while j < len(nums):
                if nums[j] == rem:
                    return i,j
                j += 1
            i += 1