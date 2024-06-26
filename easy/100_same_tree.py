from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Nếu 2 cây đều không có node nào -> 2 cây giống nhau
        if not p and not q:
            return True

        # Nếu một trong 2 cây k có nút nào hoặc chỉ cần 1 trong số các phần tử của cây không có nút nào -> nó không giống nhau
        if not p or not q or p.val != q.val:
            return False

        # Ktra đệ quy cả cây con trái và cây con phải
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
