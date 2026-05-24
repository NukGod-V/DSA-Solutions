class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        lon = 0

        for v in nset:
            if (v-1) not in nset:
                le = 0
                while (v+le) in nset:
                    le += 1
                lon = max(le,lon)
        return lon