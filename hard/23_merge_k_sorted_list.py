from typing import List, Optional

'''
    Cho một MẢNG gồm k LINKED LIST 
    Mỗi linked list được sắp xếp theo thứ tự TĂNG DẦN
    Gộp các linked list thành một linked list thống nhất được sắp xếp  
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Lấy các phần tử của linked list để cho vào mảng
        ele = []

        for l in lists:
            while l:
                ele.append(l.val) # Thêm từng phần tử vào ele
                l = l.next

        ele.sort() # Sắp xếp mảng tăng dần

        # Tạo linked list mới từ elements đã sắp xếp
        start_node = ListNode()

        # Đặt con trỏ trỏ đến nút start_node vừa tạo ở trên
        current = start_node

        for e in ele:
            current.next =ListNode(e)
            current = current.next

        return start_node.next





def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]

solution = Solution()
merged_list = solution.mergeKLists(lists)

# Function to print the linked list for verification
def print_linked_list(l):
    while l:
        print(l.val, end=" -> ")
        l = l.next
    print("None")

print_linked_list(merged_list)