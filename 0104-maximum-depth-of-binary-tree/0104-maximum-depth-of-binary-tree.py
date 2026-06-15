# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #|BFS|BFS|BFS|BFS|BFS|BFS|BFS|BFS|BFS|BFS|BFS|
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        #iterative 
        stack = [[root,1]]
        res = 0

        while stack:
            nod, dep = stack.pop()

            if nod:
                res = max(res,dep)
                stack.append([nod.left,dep + 1])
                stack.append([nod.right,dep + 1])
        return res
