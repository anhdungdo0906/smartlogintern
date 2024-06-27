class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: TreeNode, result: List[int]):
            if node:
                # duyệt từ nút gốc -> cây con trái -> cây con phải
                result.append(node.val)
                preorder(node.left, result)
                preorder(node.right, result)

        result = []
        preorder(root, result)

        return result