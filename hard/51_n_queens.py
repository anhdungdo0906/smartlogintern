'''
    Đầu vào:
    Đầu ra:
'''


from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            # state: lưu chỉ số cột của quân Hậu
            board = [] # Khởi tạo bàn cờ

            # Duyệt qua từng hàng
            for i in range(n):
                row = n * ['.'] # Khởi tạo hàng
                row[state[i]] = 'Q' # Đặt quân Hậu vào đúng hàng

                # Thêm các phần tử trong hàng vào một chuỗi và thêm vào bàn cờ
                board.append("".join(row))
            return board

        def solve(row, cols, diagonals1, diagonals2, state):
            # Trường hợp tất cả các hàng đều đã được điền
            if row == n:
                result.append(create_board(state))
                return

            # Đặt quân Hậu vào từng cột
            for col in range(n):
                # Kiểm tra xem quân Hậu có bị tấn công bởi quân Hậu khác không
                # Kiểm tra cột hiện tại có quân Hậu nào đang đứng không
                if col in cols:
                    continue

                # Kiểm tra xem quân Hậu đặt vào có bị tấn công bời quân Hậu nào trên đường chéo chính không
                # Phía dưới bên phải - phía trên bên trái
                if (row - col) in diagonals1:
                    continue

                # Kiểm tra xem quân Hậu đặt vào có bị tấn công bời quân Hậu nào trên đường chéo phụ không
                # Phía dưới bên trái - phía trên bên phải
                if (row + col) in diagonals2:
                    continue

                # Thêm các giá trị vào các tập hợp
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                state.append(col)

                # Gọi đệ quy để giải bài toán ở hàng tiếp theo
                solve(row + 1, # chuyển sang đặt quân Hậu ở hàng tiếp theo
                      cols,
                      diagonals1,
                      diagonals2,
                      state
                      )

                # Khôi phục lại trạng thái trước đó
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
                state.pop()


        # set: không chứa phần tử trùng lặp, các phần tử k thể truy cập được theo chỉ số
        result = []
        solve(0, # bắt đầu từ phần tử đầu tiên
              set(), # lưu phần tử cột bị tấn công
              set(), # lưu phẩn tử ở đường chéo chính đang bị tấn công
              set(), # lưu phần tử ở đường chéo phụ đang bị tấn công
              []) # list để kiểm soát các cột bị tấn công
        return result

sol = Solution()
example_n = 4
print(sol.solveNQueens(example_n))
