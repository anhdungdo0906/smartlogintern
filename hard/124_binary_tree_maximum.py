
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Khởi tạo đường đi có tổng nhỏ nhất là âm vô cùng
        self.max_sum = float('-inf')
        def max_path_sum(node):
            if not node:
                return 0

            # Sử dụng đệ quy, tính toán đường đi dài nhất
            # của cả cây con trái và cây con phải
            left_max = max(0, max_path_sum(node.left))
            right_max = max(0, max_path_sum(node.right))

            # tổng đường đi lớn nhất, kết thúc ở nút hiện tại
            max_end_at_node = node.val + max(left_max, right_max)

            # tổng đường đi lớn nhất qua nút hiện tại
            max_through_node = node.val + left_max + right_max

            # cập nhật tổng đường đi lớn nhất
            self.max_sum = max(self.max_sum, max_through_node, max_end_at_node)

            return max_end_at_node

        #đệ quy từ nút gốc
        max_path_sum(root)

        return self.max_sum





