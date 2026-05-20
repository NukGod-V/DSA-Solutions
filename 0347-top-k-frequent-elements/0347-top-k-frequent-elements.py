# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # res = {}
        # resl = []
        # for i in nums:
        #     res[i] = res.get(i,0) + 1
        
        # sort_dic = dict(sorted(res.items(),key = lambda, item: item[1], reverse=True))
        # i = 0
        # for e,n in sort_dic:
            

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # List of lists to store numbers by their frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Count frequencies: O(n)
        for n in nums:
            count[n] = count.get(n, 0) + 1
            
        # Place numbers into buckets: O(n)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        # Collect top k: O(n)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res