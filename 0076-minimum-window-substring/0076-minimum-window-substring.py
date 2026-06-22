class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}
        for i in t:
            countT[i] = 1 + countT.get(i,0)

        have, need = 0, len(countT)
        l = 0
        res, le = [-1, -1], float('infinity')
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                if (r - l + 1) < le:
                    res = [l, r]
                    le = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if le != float('infinity') else ""