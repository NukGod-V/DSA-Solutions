class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        resl = [[] for i in range(len(nums)+1)]

        for i in nums:
            res[i] = 1 + res.get(i,0)
        for i,n in res.items():
            resl[n].append(i)
        main_res = []

        for i in range(len(resl) -1,0,-1):
            for v in resl[i]:
                main_res.append(v)
                if len(main_res) == k:
                    return main_res
