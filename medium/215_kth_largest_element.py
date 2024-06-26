import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        # Tạo ra một min heap với k phần tử đầu tiên
        min_heap = nums[0:k]

        # Chuyển thành min heap
        # Đảm bảo rằng min_heap[0] là phần tử nhỏ nhất trong heap
        heapq.heapify(min_heap)

        for num in nums[k:]:
        # Duyệt từ phần tử k đến cuối danh sách
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                # Đẩy num vào heap
                # Loại bỏ, trả về phần phần tử nhỏ nhất từ heap

        # Trả về nút gốc, chính là phần tử thứ k lớn nhất
        return min_heap[0]
