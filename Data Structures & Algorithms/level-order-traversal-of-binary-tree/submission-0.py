# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result: List[List[int]] = []
        queue: Deque[TreeNode] = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                tmp = queue.popleft()
                level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            
            result.append(level)
        return result