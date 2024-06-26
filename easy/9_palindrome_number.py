class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x) # Chuyển đổi số nguyên x thành chuỗi
        # So sánh số đảo ngược thành chuỗi
        return str_x == self.reverse_string(str_x)

    def reverse_string(s: str) -> str:
        reversed_s = ""
        for char in s:
            reversed_s = char + reversed_s
        return reversed_s