class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        le1, le2 = len(s1), len(s2)
        if le1 > le2: return False
        
        s1count, s2count = [0] * 26, [0] * 26

        for i in range(le1):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        matches = 0

        for i in range(26):
            matches += (1 if s1count[i] == s2count[i] else 0)
        
        l = 0
        for r in range(le1,le2):
            if matches == 26: return True
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s2count[index] == s1count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            ind = ord(s2[l]) - ord('a')
            s2count[ind] -= 1

            if s2count[ind] == s1count[ind]:
                matches += 1
            elif s1count[ind] - 1 == s2count[ind]:
                matches -= 1
            l += 1
        return matches == 26