class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hm:
                return i,hm[val]
            hm[nums[i]] = i