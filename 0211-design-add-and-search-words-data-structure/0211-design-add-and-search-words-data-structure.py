class TreeNode:
    def __init__(self):
        self.char = {}
        self.endOfTWord = False 

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()


    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.char:
                curr.char[c] = TreeNode()
            curr = curr.char[c]
        curr.endOfTWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                cha = word[i]
                if cha == ".":
                    for c in curr.char.values():
                        if dfs(i + 1, c):
                            return True
                    return False
                else:
                    if cha not in curr.char:
                        return False
                    curr = curr.char[cha]
            return curr.endOfTWord
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)