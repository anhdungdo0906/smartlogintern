class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        board_size = 9
        def is_valid(board, row, col, num):
            # Kiểm tra số ở hàng hiện tại
            for x in range(board_size):
                if board[row][x] == num:
                    return False

            # Kiểm tra số ở cột hiện tại
            for x in range(board_size):
                if board[x][col] == num:
                    return False

            # Kiểm tra số ở hộp 3x3
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        def solve(board):
            for row in range(9):
                for col in range(9): # duyệt qua từng phần tử của ma trận
                    if board[row][col] == '.':  # kiểm tra phần tử duyệt qua có trống không
                        for num in '123456789':  # thử lần lượt các số từ 1-9
                            if is_valid(board, row, col, num): # kiểm tra xem có hợp lệ ở vị trí hiện tại không
                                board[row][col] = num # nếu hợp lệ, đặt số vào trong ô
                                if solve(board):
                                    return True

                        # Tính backtrack đc thể hiện qua dòng code nào ?????


                                board[row][col] = '.'  # Nếu không tìm thấy kết quả nào -> đặt về trạng thái ban đầu
                        return False  # Không thể đặt được số nào -> False
            return True  # Tất cả các phần tử đc điền thành công -> True

        solve(board) # gọi đệ quy hàm này để giải phần còn lại của bàn cờ với số được thêm vào

    '''
        Độ phức tạp thời gian: O(9^N) (xấu nhất, khi phải thử cả 9 số)
        Độ phức tạp không gian: O(N)
        với N là số lượng ô trống.
    '''