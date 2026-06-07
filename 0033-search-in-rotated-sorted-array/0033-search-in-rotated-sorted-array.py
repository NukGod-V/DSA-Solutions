class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            n = l + ((r-l)//2)
            if target == nums[n]:
                return n
            if nums[l] <= nums[n]:
                if nums[n] > target >= nums[l]:
                    r = n - 1
                else:
                    l = n + 1
            else:
                if nums[n] < target <= nums[r]:
                    l = n + 1
                else:
                    r = n - 1
        return -1