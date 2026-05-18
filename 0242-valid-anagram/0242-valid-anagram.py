class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            dict1[s[i]] = 1 + dict1.get(s[i],0)

            dict2[t[i]] = 1 + dict2.get(t[i],0)
        
        return dict1 == dict2
