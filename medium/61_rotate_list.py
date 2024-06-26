from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1.Tìm chiều dài của list
        length = 1  # bắt đầu đếm từ node head
        current = head # duyệt từ node đầu
        # duyệt cho đến khi nào k có node nào thi dừng lại
        while current.next:
            current = current.next
            length += 1

        # 2.Tính số lần xoay cần thiết
        # Giảm số lần xoay làm sao để nhỏ hơn độ dài của list
        k = k % length
        # Trường hợp k=0 nghĩa là list k cần xoay
        if k == 0:
            return head

        # 3. Tìm tail và head mới của list
        steps_to_new_tail = length - k - 1
        # length - k là vị trí mới của head trong list
        # trừ 1 đi là vị trí của tail mới

        # Tạo tail mới
        new_tail = head

        # Dịch chuyển new_tail với số bước bằng số bước đã tính ở trên
        for x in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Nốt head chính là node ngay sau node đuôi mới
        new_head = new_tail.next

        # 4. Sắp xếp lại con trỏ
        new_tail.next = None
        current.next = head # Nối đuôi vào đầu để hoàn thành việc xoay

        return new_head

def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2

solution = Solution()
new_head = solution.rotateRight(head, k)
print_list(new_head)  # Output should be [4, 5, 1, 2, 3]
