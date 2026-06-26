# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # maxd = 0
        # def rsv(root, depth):
        #     if not root: return [0] 
        #     right = rsv(root.right)
        #     if maxd < right[0]:
        #         maxd = right[0]
        #         ans.append(root.val)
        #     left = rsv(root.left)
        #     if maxd < left[0]:
        #         maxd = left[0]
        #         ans.append(root.val)
        #     return 1 + max(right[0], left[0])
        # d = rsv(root)
        # return ans

        q = collections.deque()
        q.append(root)

        while (len(q) > 0):
            rightSide = None
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                ans.append(rightSide.val)
        return ans
                
