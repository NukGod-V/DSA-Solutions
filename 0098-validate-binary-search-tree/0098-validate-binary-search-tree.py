# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # ans = True
        # if root.left:
        #     if root.left.val < root.val:
        #         ans &= True
        #     else:
        #         ans &= False
        # if root.right:
        #     if root.right.val > root.val:
        #         ans &= True
        #     else:
        #         ans &= False
        # return (ans and self.isValidBST(root.left)
        #         and self.isValidBST(root.right))
        
        def check(node, left, right):
            if not node: return True

            if not (node.val > left and node.val < right):
                return False
            
            return (check(node.left, left, node.val) and 
                    check(node.right, node.val, right))
        return check(root, float('-inf'), float('inf'))
