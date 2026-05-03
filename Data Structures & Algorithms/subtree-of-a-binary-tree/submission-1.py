# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isEqual(self, node1, node2) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        
        left_eq = self.isEqual(node1.left, node2.left)
        right_eq = self.isEqual(node1.right, node2.right)

        return left_eq and right_eq

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True
        if self.isEqual(root, subRoot):
            return True
        left_check = self.isSubtree(root.left, subRoot)
        right_check = self.isSubtree(root.right, subRoot)

        return left_check or right_check
        