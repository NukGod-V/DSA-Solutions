class Trie:
    def __init__(self):
        self.eotw = False
        self.letters = {}
    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.letters:
                cur.letters[c] = Trie()
            cur = cur.letters[c]
        cur.eotw = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.addword(w)

        result = set()
        visit = set()
        rows = len(board)
        cols = len(board[0])

        def wordsearch(root, r, c, word):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or 
                board[r][c] not in root.letters):
                return
            visit.add((r, c))
            w = board[r][c]
            root = root.letters[w]
            word += w
            if root.eotw:
                result.add(word)
            wordsearch(root, r + 1, c, word)
            wordsearch(root, r - 1, c, word)
            wordsearch(root, r, c + 1, word)
            wordsearch(root, r, c - 1, word)


            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                wordsearch(root, r, c, "")
        return list(result)