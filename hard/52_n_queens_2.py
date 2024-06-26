'''
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            # Th đặt hết toàn bộ quân hậu => có 1 cách giai
            if row == n:
                return 1

            countSolutions = 0  # Khởi tạo số lượng giải pháp là 0
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

                # Đánh dấu cột và đường chéo bị chiếm bởi quân hậu
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Đặt quân hậu ở hàng tiếp theo
                countSolutions += backtrack(row + 1)

                # Quay lui và thử cột khác
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return countSolutions

        cols = set()
        diag1 = set()
        diag2 = set()

        # Bắt đầu từ hàng đầu tiên
        return backtrack(0)
