class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def dfs(i: int) -> None:
            if i >=len(s):
                res.append(cur[::])
                return
            
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    cur.append(s[i: j+1])
                    dfs(j+1)
                    cur.pop()
        dfs(0)
        return res
    
    def palindrome(self, s: List, i: int, j: int) -> bool:
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True