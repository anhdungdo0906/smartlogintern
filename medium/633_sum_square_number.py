'''
    Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.
'''
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        leftPointer = 0
        rightPointer = int(math.sqrt(c)) # giúp thuật toán tối ưu hơn, do nếu cả a và b đều lớn hơn căn c thì

        # Phải có <=, để trong trường hợp 2 pointers bằng nhau.
        while leftPointer <= rightPointer:
            sum = leftPointer * leftPointer + rightPointer * rightPointer
            if sum == c:
                return True
            elif sum < c:
                leftPointer = leftPointer + 1
            else:
                rightPointer = rightPointer - 1

        return False



