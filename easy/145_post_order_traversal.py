class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node: TreeNode, result: List[int]):
            if node:
                # duyệt từ cây con trái -> cây con phải -> nut goc

                postorder(node.left, result)
                postorder(node.right, result)
                result.append(node.val)

        result = []
        postorder(root, result)

        return result