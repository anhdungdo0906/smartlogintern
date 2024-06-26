class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            # Nếu không có nút gốc -> Độ sâu của cây là 0 do cây rỗng
            return 0
        else:
            max_depth = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
            # Tìm kiếm chiều sâu của cây con trái và cây con phải
            # Cộng 1 là tính cả nút gốc
            return max_depth
