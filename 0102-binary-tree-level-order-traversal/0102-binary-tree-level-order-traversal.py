# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque()
        q.append(root)
        ans = []
        while len(q) > 0:
            subans = []
            # for i in q:
            #     subans.append(i)
            level_l = len(q)
            for i in range(level_l):
                node = q.popleft()
                subans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(subans)
        return ans