class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, h = 0, len(nums) - 1
        while l<=h:
            ind = (l+h) //2
            if nums[ind] == target:
                return ind
            elif nums[ind] < target:
                l = ind + 1
            else:
                h = ind - 1
        return -1