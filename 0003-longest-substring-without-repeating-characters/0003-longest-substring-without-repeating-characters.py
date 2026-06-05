class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        sub=[]
        sub.append(s[l])
        le = 0
        while r < len(s):
            if s[r] not in sub:
                sub.append(s[r])
                le = max(le, len(sub))
            else:
                l += 1
                r = l
                sub.clear()
                sub.append(s[l])
            r += 1
        return le if le else 1
