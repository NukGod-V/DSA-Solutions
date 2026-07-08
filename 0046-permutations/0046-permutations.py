class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        #base Case
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            val = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(val)
            result.extend(perms)
            nums.append(val)
        return result

